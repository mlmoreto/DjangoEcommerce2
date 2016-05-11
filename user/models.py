from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(auto_created=True)
    data = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    class Meta:
        ordering = ('username', 'email',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def __str__(self):
        return self.username