from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^add/(?P<slug>[\w_-]+)/$', views.add, name='add'),
    url(r'^del/(?P<slug>[\w_-]+)/$', views.delete, name='del'),
    url(r'^change/(?P<slug>[\w_-]+)/$', views.change, name='del')
]