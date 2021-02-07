from django                                         import forms


from apps.city.models                               import City

TIME_PERIOD = (
    ('', 'Choose...'),
    ('today',   'Today'),
    ('period',  'Number Days')
)


class WeatherSelectForm(forms.Form):
    # city            = forms.ModelChoiceField(label='City', queryset=City.objects.all(), to_field_name="city_name", blank=True,
    #                                          widget=forms.Select(attrs={'autofocus': True, 'cols': '10'})
    #                                     )    # city            = forms.ModelChoiceField(label='City', queryset=City.objects.all(), to_field_name="city_name", blank=True,
    #                                          widget=forms.Select(attrs={'autofocus': True, 'cols': '10'})
    #                                     )

    city_name       = forms.CharField(label='City Name', max_length=200)

    time_period     = forms.ChoiceField(choices=TIME_PERIOD)

    period          = forms.IntegerField(label="Period", widget=forms.NumberInput(attrs={'max': 20}))
