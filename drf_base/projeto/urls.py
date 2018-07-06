"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^foods/$', foods_list),
    url(r'^get_food/(?P<pk>[0-9]+)$', get_food),
    url(r'^add_food/$', new_food),

    url(r'^restaurants/$', restaurants_list),
    url(r'^get_restaurant/(?P<pk>[0-9]+)$', get_restaurant),
    url(r'^add_restaurant/$', new_restaurant),

	url(r'^restaurants_from_food/(?P<fk>[a-zA-Z]+)$', restaurants_list_from_food),
	url(r'^update_restaurant/(?P<pk>[0-9]+)$', update_restaurant)


]
