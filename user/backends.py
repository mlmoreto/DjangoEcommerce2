from django.utils.module_loading import import_string

from snake_shop import settings
from .models import User
from  django.contrib.auth.backends import ModelBackend


def load_backend(path):
    return import_string(path)()


class UserCustomBackend(object):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if (user.check_password(password)):
                return user
            else:
                return None
        except:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None


