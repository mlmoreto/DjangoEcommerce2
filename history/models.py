from _decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from user.models import User
from shop.models import Game
# Create your models here.

class Pedido (models.Model):
    data = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ('user','data')

    def __str__(self):
        return self.user.username + ", "+ str(self.id)

class Produto (models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    game = models.ForeignKey(Game)
    quantidade = models.PositiveIntegerField()
    valorUnitario = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Produto dos Pedidos'
        verbose_name_plural = 'Produtos dos Pedidos'
        ordering = ('pedido',)


def consumeCart(cart):
    self = Pedido()
    self.user = cart.user
    self.save()
    total = Decimal(0.0)
    for item in cart.getItens():
        p = Produto()
        p.pedido = self
        p.game = item.game
        p.quantidade = item.quantidade
        p.valorUnitario = Decimal(item.game.getValor())
        p.save()
        total += (p.quantidade*p.valorUnitario)
    self.total = total
    self.save(force_update=True)