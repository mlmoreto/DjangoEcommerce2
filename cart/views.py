from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from shop.models import Game
from user.views import isCliente
from django.contrib.auth.decorators import login_required


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
