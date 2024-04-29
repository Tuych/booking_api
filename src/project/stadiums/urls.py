from django.urls import path, include
from .views import StadiumListApiViews, StadiumDetailApiViews, StadiumImageDetailApiViews, StadiumImageListApiViews

urlpatterns = [
    path('stadium/list/', StadiumListApiViews.as_view()),
    path('stadium/detail/<int:stadium_id>/', StadiumDetailApiViews.as_view()),
    path('stadiumImage/list/', StadiumImageListApiViews.as_view()),
    path('stadiumImage/detail/<int:stadium_id>/', StadiumImageDetailApiViews.as_view())
]
