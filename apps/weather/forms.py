from django                                         import forms


from apps.city.models                               import City

TIME_PERIOD = (
    ('', 'Choose...'),
    ('today',   'Today'),
    ('1_hour',  'Minute forecast for 1 Hour'),
    ('2_days',  'Hourls forecast for 48 Hours'),
    ('7_days',  '7 Day Forecast'),
    ('5_past',  '5 Past Days')
)


class WeatherSelectForm(forms.Form):
    city_name       = forms.ModelChoiceField(label='City',
                                        queryset=City.objects.all(), to_field_name="city_name",
                                        widget=forms.Select(attrs={'autofocus': True, 'cols': '10'})
                                        )

    period          = forms.ChoiceField(choices=TIME_PERIOD)
