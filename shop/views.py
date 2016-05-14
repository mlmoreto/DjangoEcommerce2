from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Genre, Game

def home(request):
    dic = {'generos' : Genre.objects.all(),
           'games' : Game.objects.all()}
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
    dic = {
        'games' : games,
        'genero' : titulo_genero,
        'genres' : Genre.objects.all()}
    return render(request, 'jogos.html',dic)
