from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    """ class returns returns the fields bellow """
    class Meta:
        model = Property
        fields = ('title', 'address', 'city', 'state', 'price', 'sale_type', 'home_type', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'slug')

class PropertyDetailSerializer(serializers.ModelSerializer):
    """ class returns returns all fields """
    class Meta:
        model = Property
        fields = '__all__'
        lookup_field = 'slug'