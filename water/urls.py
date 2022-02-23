from django.conf.urls import url
from water import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^choose_city$', views.choose_city, name='choose_city'),
    url(r'^choose_factory$', views.choose_factory, name='choose_factory'),
    url(r'^get_data$', views.get_data, name='get_data'),
    url(r'^get_predict_data$', views.get_predict_data, name='get_predict_data'),
    url(r'^get_factory_data', views.get_factory_data, name='get_factory_data'),
    url(r'^user_login$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^predict/$', views.predict, name='predict'),
    url(r'^excel_upload/$', views.excel_upload, name='excel_upload'),


]
