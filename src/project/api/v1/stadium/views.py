from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets, permissions
from project.stadiums.models import Stadium, StadiumImage
from .serializers import StadiumImageSerializer, StadiumSerializer
from project.api.v1.permissions import AdminPermission, IsStadiumOwner, IsUser, IsAdminOrStadiumOwner
from project.booking.models import Booking
from django.db.models import Q
from django.utils import timezone
from math import radians, sin, cos, asin, sqrt



# Api for the Stadium model
class ListStadiumApiView(ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsAdminOrStadiumOwner]


class CreateStadiumApiView(CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

class DetailStadiumApiView(RetrieveUpdateDestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer





#  Api for The Stadium Image model

class ListStadiumImageApiView(ListAPIView):
    queryset = StadiumImage.objects.all()
    serializer_class = StadiumImageSerializer
    permission_classes = [AdminPermission]


class CreateStadiumImageApiView(CreateAPIView):
    queryset = StadiumImage.objects.all()
    serializer_class = StadiumImageSerializer


class DetailStadiumImage(RetrieveUpdateDestroyAPIView):
    queryset = StadiumImage.objects.all()
    serializer_class = StadiumImageSerializer



""" Option made with viewsets """
# Api for the Stadium model-viesets


class StadiumViewset(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminOrStadiumOwner]
        return [i() for i in permission_classes]
    

    


    def haversine(self, lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(radians,[lat1, lon1, lat2, lon2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2 ) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r


    def list(self, request, *args, **kwargs):
        

        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')
        lat = request.query_params.get("lat")
        lon = request.query_params.get("lon")

        if start_time and end_time:
            start_time = timezone.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S')
            end_time = timezone.datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S')

            self.queryset = Stadium.objects.exclude(
                id__in=Booking.objects.filter(
                    Q(start_time__lte=end_time, end_time__gte=start_time) |
                    Q(start_time__gte=start_time, start_time__lte=end_time) |
                    Q(end_time__gte=start_time, end_time__lte=end_time),
                    status=3
                ).values_list('stadium_id', flat=True)
            )

        if lat and lon:
            user_location  = (float(lat), float(lon))
            for stadium in self.queryset:
                stadium_location = (stadium.lat, stadium.lon)
                distance = self.haversine(*user_location,*stadium_location)
                setattr(stadium, 'distance', distance)
            self.queryset = sorted(self.queryset, key=lambda x:x.distance)
        return super().list(request, *args, **kwargs)
    


class StadiumImageViewset(viewsets.ModelViewSet):
    queryset = StadiumImage.objects.all()
    serializer_class = StadiumImageSerializer


    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsStadiumOwner]
        return [i() for i in permission_classes]
    
