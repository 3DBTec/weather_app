from .models                         import Continent
from rest_framework                  import viewsets
from rest_framework                  import permissions
from weather_app.serializers         import ContinentSerializer


class ContinentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    permission_classes = [permissions.IsAuthenticated]
