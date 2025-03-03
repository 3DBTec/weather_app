from crispy_forms.helper                            import FormHelper
from crispy_forms.layout                            import Layout, Submit, Row, Column, Fieldset, HTML

from django                                         import forms
from apps.city.models                               import City

TIME_PERIOD = (
    ('today',   'Today Only'),
    ('period',  'Number Days')
)


class WeatherSelectForm(forms.Form):
    city_choice       = forms.ModelChoiceField(label='City Choice', queryset=City.objects.all(), to_field_name="city_name", blank=True,
                                               widget=forms.Select(attrs={'autofocus': True, 'cols': '10'}))

    city_text       = forms.CharField(label='City Text', max_length=200, required=False)

    city_use_text   = forms.BooleanField(label='Use City Text', initial=False, required=False)

    time_period     = forms.ChoiceField(label='', choices=TIME_PERIOD, initial='today', widget=forms.RadioSelect())

    period          = forms.IntegerField(label="", widget=forms.NumberInput(attrs={'min': 1, 'max': 40}), initial=1, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<fieldset  class="border p-2"">'),
            HTML('<legend  class="w-auto">CITY DETAILS</legend>'),
            Row(
                Column('city_choice', css_class='form-group col-3 mb-0 med-label'),
                css_class='form-row'
            ),
            Row(
                Column('city_use_text', css_class='form-group col-3 mb-0 med-label'),
                css_class='form-row'
            ),
            Row(
                Column('city_text', css_class='form-group col-3 mb-0 med-label'),
                css_class='form-row'
            ),
            HTML('</fieldset> <p>'),

            HTML('<fieldset  class="border p-2"">'),
            HTML('<legend  class="w-auto">PERIOD DETAILS</legend>'),
            Row(
                Column('time_period',   css_class='form-group col-2 mb-0 med-label'),
                Column('period',        css_class='form-group col-1 mb-0 mt-3 med-label'),
                css_class='form-row'
            ),
            HTML('</fieldset>'),
            Submit('submit', 'Search',      css_class='btn-blue ripple mr-0 mb-3 mt-3 float-left'),
        )


class WeatherResultForm(forms.Form):

    weather         = forms.CharField(label='Weather',  max_length=200)
    temp            = forms.CharField(label='Average',  max_length=200)
    min             = forms.CharField(label='Min Temp', max_length=200)
    max             = forms.CharField(label='Max Temp', max_length=200)

    pressure        = forms.CharField(label='Pressure', max_length=200)
    humidity        = forms.CharField(label='Humidty',  max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<fieldset class="master_company_js"> <legend>Agents</legend> </fieldset>'),
            Fieldset(
                'RESULT DETAILS',
            ),
            Row(
                Column('weather',   css_class='form-group col-6 mb-0 med-label'),
                css_class='form-row'
            ),
            Row(
                Column('temp',      css_class='form-group col-2 mb-0 med-label'),
                Column('min',       css_class='form-group col-2 mb-0 med-label'),
                Column('max',       css_class='form-group col-2 mb-0 med-label'),
                css_class='form-row'
            ),
            Row(
                Column('pressure',  css_class='form-group col-6 mb-0 med-label'),
                css_class='form-row'
            ),
            Row(
                Column('humidity', css_class='form-group col-6 mb-0 med-label'),
                css_class='form-row'
            ),
        )