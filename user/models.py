from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    name = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now=True)
    birthDate = models.DateField(null=False)
    cpf = models.CharField(unique=True, max_length=15, help_text='000.000.000-00')
    rua = models.CharField(max_length=200)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    numero = models.DecimalField(decimal_places=0, max_digits=10)
    fone = models.CharField(max_length=11)
    class Meta:
        ordering = ('username', 'email',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def __str__(self):
        return self.username