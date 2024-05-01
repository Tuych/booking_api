from rest_framework import serializers
from project.stadiums.models import Stadium, StadiumImage


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['name', 'address', 'contact_number', 'booking_price_per_hour', 'description', 'lat', 'lon', 'created_date', 'update_date', 'user']



class StadiumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumImage
        fields = ['image', 'is_main', 'stadium']



