from django.conf.urls import url

from . import views

app_name = 'signin'

urlpatterns = [
    
    url(r'^registration/$',views.registration, name='registration'),
    url(r'^login/$',views.login, name='login'),
    url(r'^logout/$',views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^send/$', views.email,name='email'),



]