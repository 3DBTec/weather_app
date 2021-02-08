from django.views.generic                                                           import View
from django.shortcuts                                                               import render, redirect, reverse

from django.contrib.auth.models                                                     import User, Group
from rest_framework                                                                 import viewsets
from rest_framework                                                                 import permissions
from weather_app.serializers                                                        import UserSerializer, GroupSerializer

from .                                                                              import template
from API                                                                            import open_weather_app

from .forms                                                                         import WeatherSelectForm
from .forms                                                                         import WeatherResultForm


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class WeatherSearchView(View):
    template_search  = template.path('WeatherSearchView')
    template_results = template.path('WeatherResultsView')

    def get(self, request, *args, **kwargs):

        if not request.GET:

            form = WeatherSelectForm(request.GET or None)
            context = {'form': form}

            return render(request, template_name=self.template_search, context=context)

        else:

            form = WeatherSelectForm(request.GET or None)

            city_use_text   = 'off'
            city_choice     = form.data['city_choice']
            city_text       = form.data['city_text']
            time_period     = form.data['time_period']
            period          = form.data['period']

            if 'city_use_text' in form.changed_data:
                city_use_text = form.data['city_use_text']

            graphs = {}

            if 'on' in city_use_text:
                city_name = city_text
            else:
                city_name = city_choice

            if time_period == 'today':
                results     = open_weather_app.get_current_weather_by_city_name(city_name)

                if results:

                    initial = {'weather':   results['weather'],
                               'temp':      results['temp'],
                               'min':       results['min'],
                               'max':       results['max'],
                               'pressure':  results['pressure'],
                               'humidity':  results['humidity'],
                               }
                    form = WeatherResultForm(initial=initial)

            elif time_period == 'period':
                results, graphs    = open_weather_app.get_period_weather_by_city_name(city_name, period)

            context     = {'form': form, 'city_name': city_name, 'results': results, 'time_period': time_period, 'period': period,
                           'graphs': graphs}

            return render(request, template_name=self.template_results, context=context)
