from django.contrib.auth.models         import User, Group
from apps.city.models                   import City
from apps.country.models                import Country
from rest_framework                     import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CountrySerializer(serializers.ModelSerializer):
    continent = serializers.ChoiceField(choices=Country.CONTINENTS)

    class Meta:
        model = Country
        fields = ['country_name', 'country_code', 'continent']


class CitySerializer(serializers.HyperlinkedModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ['city_name', 'city_code', 'geo_latitude', 'geo_longitude', 'country']

    def create(self, validated_data):
        country_data = validated_data.pop('country')
        country = Country.objects.create(**country_data)
        city = City.objects.create(country=country, **validated_data)
        return city
