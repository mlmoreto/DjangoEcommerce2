from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Genre, Game

def home(request):
    dic = {'generos' : Genre.objects.all(),
           'games' : Game.objects.all()}
    return render(request, 'home.html', dic)
