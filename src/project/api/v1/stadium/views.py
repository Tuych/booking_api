from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from project.stadiums.models import Stadium, StadiumImage
from .serializers import StadiumImageSerializer, StadiumSerializer
from project.api.v1.permissions import AdminPermission, IsStadiumOwner, IsUser



# Api for the Stadium model
class ListStadiumApiView(ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    # permission_classes = [AdminPermission]


class CreateStadiumApiView(CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

class DetailStadiumApiView(RetrieveUpdateDestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer





#  Api for The StadiumImage model

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