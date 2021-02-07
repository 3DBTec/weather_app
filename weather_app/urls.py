"""weather_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib                     import admin
from django.urls                        import path, include
from django.conf                        import settings
from django.views.generic.base          import TemplateView

from django.contrib.staticfiles.urls    import staticfiles_urlpatterns

from rest_framework                     import routers
from apps.weather.views                 import UserViewSet
from apps.weather.views                 import GroupViewSet
from apps.country.views                 import CountryViewSet
from apps.city.views                    import CityViewSet

from apps.weather.views                 import WeatherSearchView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users',       UserViewSet)
router.register(r'groups',      GroupViewSet)
router.register(r'countrys',    CountryViewSet)
router.register(r'citys',       CityViewSet)

urlpatterns = [
    path('',            TemplateView.as_view(template_name='home.html'), name='home'),
    path('search',      WeatherSearchView.as_view(),                     name='weather_search'),
    path('rest_api/',   include(router.urls),                            name='rest_api'),
    path('api-auth/',   include('rest_framework.urls')),
    path('admin/',      admin.site.urls,                                 name='admin'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

