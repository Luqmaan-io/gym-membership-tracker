from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Gym(models.Model):
    owner = models.ForeignKey(
    User, on_delete=models.PROTECT, related_name="gyms"
)
    gym_name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.gym_name

    class Meta:
        ordering = ['-date_joined']
