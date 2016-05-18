from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from shop.models import Genre, Game

def home(request):
    games = Game.objects.all().order_by('created').reverse()[:8]
    paginator = Paginator(games, 8) #8 jogos por página
    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)
    dic = {'generos' : Genre.objects.all(),
           'games' : games,
           'page' : page}
    return render(request, 'home.html', dic)

def sobre(request):
    return render(request, 'sobre.html')

def jogos(request,slug):
    jogos = Game.objects.all()
    games = []
    titulo_genero = ""
    for j in jogos:
        genres = j.genres.all()
        for g in genres:
            if(g.slug == slug):
                games.append(j)
                titulo_genero = g.title
                break
    paginator = Paginator(games, 8) #8 jogos por página
    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)
    dic = {
        'games' : games,
        'page' :page,
        'genero' : titulo_genero,
        'genres' : Genre.objects.all()}
    return render(request, 'jogos.html',dic)

def detalhes(request, slug):
    game = get_object_or_404(Game, slug=slug)
    dic = {
        'game' : game}
    return render(request, 'detalhes.html', dic)
