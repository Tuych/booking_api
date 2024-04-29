from rest_framework import serializers
from .models import Stadium, StadiumImage



class StadiumSerializer(serializers.ModelSerializer):


    class Meta:
        model = Stadium
        fields = '__all__'



class StadiumImageSerializer(serializers.ModelSerializer):


    class Meta:
        model = StadiumImage
        fields = ['id', 'image', 'is_main', 'stadium']