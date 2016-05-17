from django.utils.module_loading import import_string

from snake_shop import settings
from .models import User
from  django.contrib.auth.backends import ModelBackend


def load_backend(path):
    return import_string(path)()


class UserCustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.filter(username=username)[0]
            if (user.check_password(password)):
                setattr(user, 'backend', load_backend('user.backends.UserCustomBackend'))
                return user
            else:
                return None
        except:
            return None