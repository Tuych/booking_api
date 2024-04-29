from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import StadiumSerializer, StadiumImageSerializer
from .models import Stadium, StadiumImage




#  rest_framework.views --- APIView
class StadiumListApiViews(APIView):

    def get(self, request, *args, **kwargs):
        stadium = Stadium.objects.all()
        serializer = StadiumSerializer(stadium, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        serializer = StadiumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StadiumDetailApiViews(APIView):
    def get_object(self, stadium_id):
        try:
            stadium = Stadium.objects.get(id=stadium_id)
        except Stadium.DoesNotExist:
            stadium = None
        return stadium


    def get(self, request, stadium_id, *args, **kwargs):

        stadium = self.get_object(stadium_id)
        if not stadium:
            return Response({"error":"stadion_id doesnt find"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StadiumSerializer(stadium)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, stadium_id, *args, **kwargs):
        stadium = self.get_object(stadium_id)
        if not stadium:
            return Response({"error":"stadion_id doesnt find"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StadiumSerializer(instance=stadium, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, stadium_id, *args, **kwargs):
        stadium = self.get_object(stadium_id)
        if not stadium:
            return Response({"error":"stadion_id doesnt find"}, status=status.HTTP_404_NOT_FOUND)

        stadium.delete()
        return Response({"message":"stadium deleted"})
    



class StadiumImageListApiViews(APIView):
    def get(self, request, *args, **kwargs):
        stadium_image = StadiumImage.objects.all()
        serializer = StadiumImageSerializer(stadium_image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        serializer = StadiumImageSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StadiumImageDetailApiViews(APIView):
    def get(self, request, stadium_id, *args, **kwargs):
        stadium_image = get_object_or_404(StadiumImage, stadium=stadium_id)
        serializer = StadiumImageSerializer(stadium_image)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, stadium_id, *args, **kwargs):
        stadium_image = get_object_or_404(StadiumImage, stadium=stadium_id)
        serializer = StadiumImageSerializer(instance=stadium_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, stadium_id, *args, **kwargs):
        stadium_image = get_object_or_404(StadiumImage, stadium=stadium_id)
        stadium_image.delete()
        return Response({"message":"stadium image deleted"})

