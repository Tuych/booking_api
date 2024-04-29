from django.urls import path, include
from .views import BookingListApiViews, BookingDeatilApiViews
urlpatterns = [
    path('list/', BookingListApiViews.as_view()),
    path('detail/<int:user_id>/', BookingDeatilApiViews.as_view()),
   
]
