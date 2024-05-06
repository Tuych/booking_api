from rest_framework import viewsets, permissions
from project.booking.models import Booking
from .serializers import BookingSerializer
from project.api.v1.permissions import IsStadiumOwner, AdminPermission, IsUser,IsAdminOrStadiumOwner


class BookingVievset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        
        if self.action == 'create':
            permissions_classes = [IsUser]
        elif self.action == 'list':
            permissions_classes = [IsAdminOrStadiumOwner]
        elif self.action == 'destroy':
            permissions_classes = [IsStadiumOwner]
        
        return [i() for i in permissions_classes]
            
        
        

