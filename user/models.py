from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    name = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now=True)
    birthDate = models.DateField()
    cpf = models.CharField(max_length=15)
    rua = models.CharField(max_length=200)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    numero = models.DecimalField(decimal_places=0, max_digits=10)
    fone = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    ##Field para verificação de necessiade de troca de senha
    is_password_generated = models.BooleanField(default=False)

    #Fields for validation, permissions
    is_staff = False
    is_active = True
    is_superuser = False
    user_permissions = None

    def has_perms(self, perm_list, obj=None):
        return False

    def has_module_perms(self, app_label):
        return False

    def has_module_perms(self, app_label):
        return False
    #Fim

    class Meta:
        ordering = ('username', 'email',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if(not self.has_usable_password()):
            self.set_password(self.password)
        try:
            super(User, self).save(*args, **kwargs)
        except:
            super(User, self).save(*args, **kwargs, force_update=True)

    def getCart(self):
        from cart.models import Cart
        try:
            car = Cart.objects.get(user=self)
            return car
        except:
            car = Cart()
            car.user = self
            car.save()
            return car

    def getHistory(self):
        from history.models import Pedido
        return Pedido.objects.filter(user=self).order_by('id').reverse()