from django.contrib                     import admin
from django.urls                        import path, include
from django.conf                        import settings
from django.views.generic.base          import TemplateView

from django.contrib.staticfiles.urls    import staticfiles_urlpatterns

from .views                             import WeatherSearchView


urlpatterns = [

    path('',                        WeatherSearchView.as_view(), name='weather_search'),
    # path('document/',               include('npo_project.apps.document.urls')),
    # path('graph/',                  include('npo_project.apps.graphs.urls')),

    path('admin/',                  admin.site.urls),
    # path('entity/',                 include('npo_project.apps.entity.urls')),
    # path('questions/',              include('npo_project.apps.question.urls')),
    # path('response/',               include('npo_project.apps.response.urls'))

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
