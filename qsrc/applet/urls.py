from django.conf.urls import url
from . import views



urlpatterns = [
    

    url(r'^$', views.index , name='index'),
    url(r'^youtube', views.youtube , name='youtube'),
    url(r'^upload', views.data_upload , name='data_upload'),

]
