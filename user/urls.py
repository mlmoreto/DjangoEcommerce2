from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.show_user),
    url(r'login/$', views.login_user),
    url(r'cadastro/$', views.cadastro_user),
    url(r'logout/$', views.deslogar),
]