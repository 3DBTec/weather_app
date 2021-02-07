from django.views.generic                                                           import View
from django.shortcuts                                                               import render, redirect, reverse


from .                                                                              import template

from API                                                                            import open_weather_app

from .forms                                                                         import WeatherSelectForm
from .forms                                                                         import WeatherResultForm


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

            # city        = form.data['city']
            city_name   = form.data['city_name']
            time_period = form.data['time_period']
            period      = form.data['period']

            graphs = {}

            if time_period == 'today':
                results     = open_weather_app.get_current_weather_by_city_name(city_name)

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
