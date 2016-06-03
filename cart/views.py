import random

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from shop.models import Game
from user.views import isCliente
from django.contrib.auth.decorators import login_required
from snake_shop import settings


@login_required(login_url='/user/login/')
def add(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if (isCliente(request.user)):
        cart = request.user.getCart()
        if (game.available and game.stock >= 1):
            cart.addItem(id_game=game.id)
        else:
            dic = {'mensagem': game.title,
                   'body': 'O jogo ' + game.title + ' não tem estoque suficiente ou está indispónivel.'}
            return render(request, 'erro_jogo.html', dic)
    return HttpResponseRedirect(reverse('user.views.meu_carrinho'))


@login_required(login_url='/user/login/')
def delete(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if (isCliente(request.user)):
        cart = request.user.getCart()
        cart.deleteItem(id_game=game.id)
    return HttpResponseRedirect(reverse('user.views.meu_carrinho'))


@login_required(login_url='/user/login/')
def change(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if (isCliente(request.user) and request.method == 'GET'):
        cart = request.user.getCart()
        quantidade = int(request.GET.get('quantidade'))
        if (quantidade >= 1):
            if (game.available and game.stock >= quantidade):
                cart.addItem(id_game=game.id, quantidade=quantidade)
            else:
                dic = {'mensagem': game.title,
                       'body': 'O jogo ' + game.title + ' não tem estoque suficiente ou está indispónivel.'}
                return render(request, 'erro_jogo.html', dic)
        else:
            cart.deleteItem(id_game=game.id)
    return HttpResponseRedirect(reverse('user.views.meu_carrinho'))


@login_required(login_url='/user/login/')
def submit(request):
    if (isCliente(request.user)):
        cart = request.user.getCart()
        if (cart.size > 0):
            if (cart.isValid()):
                from history.models import consumeCart
                consumeCart(cart=cart)
                msg = 'Olá ' + request.user.name + '\n'
                for i in cart.getItens():
                    msg += i.game.title + ", serial(s): "
                    for i in range(0,i.quantidade):
                        msg += gerarCod()+'; '
                    msg += '\n'

                msg += '\nObrigado por comprar pela nossa loja SNAKEGAMES.'

                to_list = [request.user.email]
                try:
                    send_mail('Compra SNAKEGAMES', msg, settings.EMAIL_HOST_USER,
                          to_list, fail_silently=True)
                except:
                    print('Sem internet')
                cart.delete()
                dic = {'mensagem': 'Compra finalizada com sucesso',
                       'body': 'Por favor verefique seu email para receber os produtos.'}
                return render(request, 'sucesso_compra.html', dic)
            else:
                dic = {'mensagem': 'Carrinho contem itens esgotados',
                   'body': 'Pedimos desculpas pelo inconveniente.'}
                return render(request, 'erro_compra.html', dic)
        else:
            dic = {'mensagem': 'Carrinho vazio',
                   'body': 'Por favor coloque um item no carrinho para finalizar a compra.'}
            return render(request, 'erro_compra.html', dic)


def gerarCod():
    letras = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r',
              't', 'y', 'u', 'i', 'o', 'p'] * 5
    random.shuffle(letras)
    cod = ''
    for c in letras[:20]:
        cod += c
    return cod
