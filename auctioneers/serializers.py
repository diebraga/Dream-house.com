from rest_framework import serializers
from .models import Auctioneer

class AuctioneerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auctioneer
        fields = '__all__'
