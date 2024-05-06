from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingVievset

router = DefaultRouter()
router.register(r'mybooking', BookingVievset )


urlpatterns = [
    path('', include(router.urls))
    
]