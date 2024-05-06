from rest_framework import serializers
from project.stadiums.models import Stadium, StadiumImage


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['id', 'name', 'address', 'contact_number', 'booking_price_per_hour', 'description', 'lat', 'lon', 'created_date', 'update_date', 'user']


    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)





class StadiumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumImage
        fields = ['id', 'image', 'is_main', 'stadium']



