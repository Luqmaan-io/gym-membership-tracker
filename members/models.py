from django.db import models
from gym.models import Gym

# Create your models here.
MEMBER_STATUS = ((0, "Inactive"), (1, "Active"), (2, "Suspended"), (3, "Frozen"))

class Member(models.Model):
    gym = models.ForeignKey(
        Gym, on_delete=models.PROTECT, related_name="members"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    emergency_contact = models.CharField(max_length=200)
    emergency_phone_number = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=MEMBER_STATUS, default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['-date_joined']

