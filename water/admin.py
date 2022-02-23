from django.contrib import admin
from water.models import *
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['username','password']


class CityAdmin(admin.ModelAdmin):
    list_display = ['city']

class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name','date','ph','cod','nh4']


admin.site.register(UserProfile)
admin.site.register(City,CityAdmin)
admin.site.register(Province,UserProfileAdmin)
admin.site.register(Factory,FactoryAdmin)