import json
import os
import time
# from asyncio.log import logger
from asyncio.log import logger
from threading import Thread

import pandas as pd

import xlrd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.core import serializers
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from water.models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

from test import Predict_model, Predict_model1, Predict_model2, Change_data

# Create your views here.
from water_quality_inspection.settings import BASE_DIR


# 分页
def pages(request, fac_data):
    paginator = Paginator(fac_data, 10)

    # 获取url页面参数
    cur_page = request.GET.get('page', 1)
    cur_page = int(cur_page)
    page = paginator.page(cur_page)
    # 获取当前页
    curr_page = page.number
    page_range = list(range(max(curr_page - 8, 1), curr_page)) + \
                 list(range(curr_page, min(curr_page + 8, paginator.num_pages) + 1))
    # 加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 首页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    # 尾页
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    page = {
        'page': page,
        'curr_page': curr_page,
        'page_range': page_range
    }

    return page


# 首页
def index(request):
    province = Province.objects.all()
    fac_data = Factory.objects.all()

    page = pages(request, fac_data)

    return render(request, 'water/index.html', locals())


# 管理员预测页
def predict(request):
    province = Province.objects.all()
    fac_data = Factory.objects.all()
    return render(request, 'water/predict.html', locals())


# 通过选择省份，获取省份的id，筛选出省份的所有城市
def choose_city(request):
    pid = request.GET.get('pid')
    city = City.objects.filter(province_id=pid)
    ret = serializers.serialize('json', city)
    return HttpResponse(json.dumps(ret))


# 通过选择城市，获取城市的id，筛选出城市的所有工厂
def choose_factory(request):
    cid = request.GET.get('cid')
    fac = Factory.objects.filter(city_id=cid)
    ret = serializers.serialize('json', fac)
    print(type(ret))
    print(ret)
    return HttpResponse(json.dumps(ret))


# 通过选择工厂，获取工厂的水质信息
def get_data(request):
    fac_name = request.GET.get('name')

    fac = Factory.objects.filter(name=fac_name)
    fac = fac[len(fac)-24:len(fac)]
    print(len(fac))
    print(type(fac))
    ret = serializers.serialize('json', fac)
    return HttpResponse(json.dumps(ret))


# 根据所选的工厂预测相应的值
def get_predict_data(request):
    # fac_name = request.GET.get('name')[:-7]
    # fac = Factory.objects.filter(name=fac_name)
    # ret = serializers.serialize('json', fac)

    fac_name = request.GET.get('name')[:-7]
    fac = Factory.objects.filter(name=fac_name)

    pred_data_list = []
    list_time = []
    list_ph = []
    list_cod = []
    list_nh4 = []
    for i in fac:
        list_time.append(i.date)
        list_ph.append(i.ph)
        list_cod.append(i.cod)
        list_nh4.append(i.nh4)
    # ori_data = {
    #     'ph': list_ph,
    #     'cod': list_cod,
    #     'nh4': list_nh4,
    # }
    dateframe = Change_data(list_time, list_ph, list_cod, list_nh4).change_dateframe()
    print(dateframe)
    print(type(dateframe))
    ph = Predict_model(dateframe).load_data()[-24:]
    cod = Predict_model1(dateframe).load_data()[-24:]
    nh4 = Predict_model2(dateframe).load_data()[-24:]
    # pred_data = {}
    print(nh4)
    list_data = []

    for x, y, z in zip(ph[:, 0].tolist(), cod[:, 0].tolist(), nh4[:, 0].tolist()):
        pred_data = {}
        if y < 50 and z < 5:
            if x > 9 or x < 6:
                pred_data['level'] = '废水'
                pred_data['facname'] = fac_name
                pred_data['ph'] = x
                pred_data['cod'] = y
                pred_data['nh4'] = z
                list_data.append(pred_data)
            else:
                pred_data['level'] = 'A1'
                pred_data['facname'] = fac_name
                pred_data['ph'] = x
                pred_data['cod'] = y
                pred_data['nh4'] = z
                list_data.append(pred_data)
        elif y > 80 or z > 8:
            pred_data['level'] = '废水'
            pred_data['facname'] = fac_name
            pred_data['ph'] = x
            pred_data['cod'] = y
            pred_data['nh4'] = z
            list_data.append(pred_data)
        else:
            pred_data['level'] = 'B1'
            pred_data['facname'] = fac_name
            pred_data['ph'] = x
            pred_data['cod'] = y
            pred_data['nh4'] = z
            list_data.append(pred_data)

    print(list_data)
    print(type(list_data))

    aa = json.dumps(list_data)
    print(aa)
    print(type(aa))
    ret = serializers.serialize('json', fac)
    # a = serializers.serialize('json', [pred_data])
    # print(a)

    return HttpResponse(aa)


# 根据时间选择工厂的数据
def get_factory_data(request):
    time = request.GET.get('time')

    fac = Factory.objects.filter(date__startswith=time)
    ret = serializers.serialize('json', fac)
    return HttpResponse(json.dumps(ret))


# 文件上传
def excel_upload(request):
    if request.method == 'POST':
        f = request.FILES.get('myfile')
        city_id = request.POST.get('pid')
        excel_type = f.name.split('.')[1]
        fac_name = f.name.split('.')[0]
        if excel_type in ['xlsx', 'xls']:
            # 开始解析上传的excel表格
            wb = xlrd.open_workbook(filename=None, file_contents=f.read())
            print(wb)
            # table = wb.sheet_by_index(1)
            table = wb.sheet_by_name('监测数据报表')
            # table = wb.sheets()[0]

            rows = table.nrows  # 总行数
            print(table.row_values(2), rows)
            try:
                for i in range(4, rows):
                    rowVlaues = table.row_values(i)
                    city = City.objects.filter(id=city_id).first()
                    Factory.objects.create(city=city, name=fac_name, date=rowVlaues[0], ph=rowVlaues[1]
                                           , cod=rowVlaues[2], nh4=rowVlaues[3], level='')
            except:
                logger.error('解析excel文件或者数据插入错误')
            return render(request, 'water/predict.html', {'message': '导入成功'})
        else:
            logger.error('上传文件类型错误！')
            # return render(request, 'water/predict.html', {'message': '导入失败'})
            return HttpResponse('上传文件类型错误')


# 管理员登录
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('predict'))
            else:
                # 账户未激活，禁止登录
                return HttpResponse("你的账户未激活")
        else:
            # 提供的登录凭据有问题，不能登录
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("不能提供登录")
    else:

        return render(request, 'water/login.html', {})


# 管理员退出
@login_required
def user_logout(request):
    # 可以确定用户已登录，因此直接退出
    logout(request)
    # 把用户带回首页
    return HttpResponseRedirect(reverse('index'))
