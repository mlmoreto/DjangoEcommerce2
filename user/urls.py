from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.show_user),
    url(r'login/$', views.login_user),
    url(r'cadastro/$', views.cadastro_user),
    url(r'logout/$', views.deslogar),
    url(r'recuperar/$', views.recuperarSenha),
    url(r'minha-conta/$',views.minha_conta),
    url(r'minha-conta/carrinho/$',views.meu_carrinho),
    url(r'minha-conta/historico/$',views.meu_historico),
    url(r'minha-conta/meus-dados/$',views.meus_dados)
]