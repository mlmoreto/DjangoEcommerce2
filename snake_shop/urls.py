"""snake_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^detalhes/(?P<slug>[\w_-]+)/$', views.detalhes, name='detalhes'),
    url(r'^(?P<slug>[\w-]+)/$',views.jogos, name='jogos'),
    url(r'^$', include('shop.urls'))## cuidado é & e não $-- é $ do outro não roda
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
