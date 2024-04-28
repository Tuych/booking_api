from django.db import models
from project.user.models import User
from project.stadiums.models import Stadium

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "%s - %s" %(self.user, self.stadium)
    
