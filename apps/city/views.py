from .models                         import City
from rest_framework                  import viewsets
from rest_framework                  import permissions
from weather_app.serializers         import CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = City.objects.all().select_related('country')
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'country'
    lookup_url_kwarg = 'country'
