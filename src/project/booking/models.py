from django.db import models
from project.user.models import User
from project.stadiums.models import Stadium

class Booking(models.Model):
    status_choices = (
        (1, 'active'),
        (2, 'cancel'),
        (3, 'book')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.SmallIntegerField(choices=status_choices, null=False,blank=False, default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "%s - %s" %(self.user, self.stadium)
    
