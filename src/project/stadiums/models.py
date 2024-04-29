from django.db import models
from project.user.models import User

class Stadium(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=400, null=False, blank=False)
    contact_number = models.CharField(max_length=13, null=False, blank=False)
    booking_price_per_hour = models.FloatField(null=False, blank=False)
    description = models.TextField()
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return self.name


class StadiumImage(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_main = models.ImageField(upload_to='images/', null=True, blank=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return "%s - %s" %(self.stadium, self.is_main)