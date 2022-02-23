from django import template

from water.models import *

#注册我们自定义的标签，只有注册过的标签，系统才能认识你，这是固定写法
register = template.Library()    #register的名字是固定的,不可改变


# @register.inclusion_tag('water/cats.html')
# def get_category_list(cat=None):
#     return {'cats': Category.objects.all(),
#             'act_cat':cat}
