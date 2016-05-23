from _decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ('title',)

    def __str__(self):
        return self.title

class Game(models.Model):
    title = models.CharField(max_length=130, db_index=True)
    slug = models.CharField(max_length=130, db_index=True, unique=True)
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True)
    card = models.ImageField(upload_to='logos/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.1)])
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    genres = models.ManyToManyField(Genre, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000, default="")
    multiplayer = models.BooleanField(default=False)
    cooperation = models.BooleanField(default=False)
    offline = models.BooleanField(default=True)
    specifications = models.TextField(max_length=1000, default="")
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0.1)])
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def getValor(self):
        des = self.desconto / Decimal(100.0)
        valor = self.price
        valor = valor - (valor * des)
        return valor