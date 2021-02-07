from .models                         import Country
from rest_framework                  import viewsets
from rest_framework                  import permissions
from weather_app.serializers         import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = Country.objects.all().select_related('continent')
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'continent'
    lookup_url_kwarg = 'continent'
