from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ListStadiumApiView, CreateStadiumApiView, DetailStadiumApiView,
                    ListStadiumImageApiView, CreateStadiumImageApiView, DetailStadiumImage, StadiumViewset, StadiumImageViewset)


""" Option made with viewsets """
# url for the Stadium model 
router = DefaultRouter()
router.register(r"stadium", StadiumViewset)
router.register(r"stadium_image", StadiumImageViewset)



urlpatterns = [
    path('', ListStadiumApiView.as_view() ),
    path('create/', CreateStadiumApiView.as_view() ),
    path('detail/<int:pk>/', DetailStadiumApiView.as_view() ),
    path('image/', ListStadiumImageApiView.as_view() ),
    path('image/create/', CreateStadiumImageApiView.as_view() ),
    path('image/detail/<int:pk>/', DetailStadiumImage.as_view() ),
    path('my/', include(router.urls))

]
