from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializer import BookingSerializers
from .models import Booking


class BookingListApiViews(APIView):
    
    def get(self, request, *args, **kwargs):
        booking = Booking.objects.all()
        serializer = BookingSerializers(booking, many=True)
        return Response(serializer, status=status.HTTP_200_OK)
    

    
    def post(self, request, *args, **kwargs):
        serializer = BookingSerializers(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookingDeatilApiViews(APIView):
    def get(self, request, user_id, *args, **kwargs):
        booking = get_object_or_404(Booking, user=user_id)
        serializer = BookingSerializers(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, user_id, *args, **kwargs):
        booking = get_object_or_404(Booking, user=user_id)
        serializer = BookingSerializers(instance=booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, user_id, *args, **kwargs):
        booking = get_object_or_404(Booking, user=user_id)
        booking.delete()
        return Response({'message':'booking deleted'}, status=status.HTTP_204_NO_CONTENT)
