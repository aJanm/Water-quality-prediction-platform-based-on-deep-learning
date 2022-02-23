import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'water_quality_inspection.settings')
import django

django.setup()

from water.models import Province, City, Factory


def populate():
    # 首先创建一些字典，列出想添加到各分类的网页
    # 然后创建一个嵌套字典，设置各分类
    # 这么做看起来不易理解，但是便于迭代，方便为模型添加数据

    panzhihu = [
        {"name": "并港口",
         "date": "20200121000000",
         'ph': '6.8',
         'cod': '32',
         'nh4': '8.6',
         'level': '一级',
         },
        {"name": "啊实打实",
         "date": "20200121000100",
         'ph': '7.8',
         'cod': '36.87',
         'nh4': '5.6',
         'level': '四级',
         },
    ]
    bejing = [
        {"name": "全为",
         "date": "20200121000000",
         'ph': '6.38',
         'cod': '32.78',
         'nh4': '8.6',
         'level': '二级',
         },
        {"name": "佛如",
         "date": "20200121000100",
         'ph': '8.8',
         'cod': '33.87',
         'nh4': '6.16',
         'level': '三级',
         },
    ]

    sichuang = [
        {"name": "巴中",
         },
        {"name": "成都",
         },
        {"name": "达州",
         },
        {"name": "攀枝花",
         },
    ]

    bejing_city = [
        {"name": "北京",
         },
    ]
    shanghai_city = [
        {"name": "上海",
         },
    ]
    provinces = {"四川": {"city": sichuang},
                 "北京": {"city": bejing_city},
                 "上海": {"city": shanghai_city}}

    city = {
        "攀枝花": {"name": panzhihu},
        "北京": {"name": bejing},
        # '上海':{'name':shanghai},
    }
    cits = []
    for province, province_data in provinces.items():
        c = add_province(province)
        for p in province_data["city"]:
            cit = add_city(c, p['name'])
            cits.append(cit)
        for cit1, city_data in city.items():
            for ci,cit in zip(city_data['name'],cits):
                add_factory(cit, ci['name'], ci['date'], ci['ph'], ci['cod'], ci['nh4'], ci['level'])


def add_province(name):
    c = Province.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_city(province, city):
    p = City.objects.get_or_create(province=province, city=city)[0]
    p.city = city
    p.save()
    return p


def add_factory(city, name, date, ph, cod, nh4, level):
    f = Factory.objects.get_or_create(city=city, name=name, date=date, ph=ph, cod=cod, nh4=nh4, level=level)[0]
    f.name = name
    f.date = date

    f.ph = ph
    f.cod = cod
    f.nh4 = nh4
    f.level = level
    f.save()
    return f




# 从这开始执行
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
