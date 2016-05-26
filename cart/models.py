from django.db import models
from user.models import User
from shop.models import Game
from django.core.validators import MinValueValidator


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    update = models.DateField(auto_now_add=True)
    size = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'
        ordering = ('user',)

    def __str__(self):
        return self.user.username

    def addItem(self, id_game, quantidade=1):
        game = Game.objects.get(id=id_game)
        item = Item()
        item.cart = self
        item.game = game
        item.quantidade = quantidade
        try:
            item.save()
            self.size += 1
            self.save()
        except:
            if (quantidade >= 1):
                item = Item.objects.get(game_id=id_game, cart_id=self.id)
                item.quantidade = quantidade
                item.save(force_update=True)

    def deleteItem(self, id_game):
        item = Item.objects.get(game_id=id_game, cart_id=self.id)
        item.delete()
        self.size += -1
        if(self.size < 0):
            self.size = 0
        self.save()

    def getItens(self):
        itens = Item.objects.filter(cart_id=self.id)
        return itens


class Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens do Carrinho'
        ordering = ('cart',)
        unique_together = ('cart', 'game')

    def __str__(self):
        return self.cart.user.username

    def getTotal(self):
        return self.quantidade * self.game.getValor()
