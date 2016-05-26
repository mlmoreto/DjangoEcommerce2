from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^sobre/',views.sobre),
    url(r'^search/',views.searchGames),
    url(r'^detalhes/(?P<slug>[\w_-]+)/$', views.detalhes, name='detalhes'),
    url(r'^cart/', include('cart.urls')),
    url(r'^(?P<slug>[\w-]+)/$', views.jogos, name='jogos'),
]