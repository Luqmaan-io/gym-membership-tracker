from django.db import models
from members.models import Member

# Create your models here.

class Attendance(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="attendances"
    )
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.first_name} - {self.date}"
    
    class Meta:
        ordering = ['-check_in_time']
