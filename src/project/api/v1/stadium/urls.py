from django.urls import path, include
from .views import (ListStadiumApiView, CreateStadiumApiView, DetailStadiumApiView,
                    ListStadiumImageApiView, CreateStadiumImageApiView, DetailStadiumImage)

urlpatterns = [
    path('', ListStadiumApiView.as_view() ),
    path('create/', CreateStadiumApiView.as_view() ),
    path('detail/<int:pk>/', DetailStadiumApiView.as_view() ),
    path('image/', ListStadiumImageApiView.as_view() ),
    path('image/create/', CreateStadiumImageApiView.as_view() ),
    path('image/detail/<int:pk>/', DetailStadiumImage.as_view() ),
]
