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
from django.urls                        import path
from django.conf                        import settings
from django.views.generic.base          import TemplateView

from django.contrib.staticfiles.urls    import staticfiles_urlpatterns


from apps.weather.views                 import WeatherSearchView
from apps.weather.views                 import LineChartJSONView
from apps.weather.views                 import line_chart
from apps.weather.views                 import line_chart_json

urlpatterns = [
    path('',                 WeatherSearchView.as_view(),    name='weather_search'),
    path('admin/',           admin.site.urls),

    path('line_chart/',      line_chart,                     name='line_chart'),
    path('bar_chart/',       TemplateView.as_view(template_name='weather/bar_chart.html')),
    path('line_chart_JSON/', line_chart_json,                name='line_chart_json'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

