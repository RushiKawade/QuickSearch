from django.conf.urls import include,url
from django.contrib import admin
from applet import views
from realtime import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', include('applet.urls')),
    url(r'^signin/', include('signin.urls')),
    url(r'^recent', views.firebase , name='firebase'),

]
