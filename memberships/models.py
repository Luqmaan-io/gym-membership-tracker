from django.db import models
from gym.models import Gym

# Create your models here.
PLAN_STATUS = ((0, "Inactive"), (1, "Active"))

class MembershipPlan(models.Model):
    gym = models.ForeignKey(
        Gym, on_delete=models.CASCADE, related_name="membership_plans"
    )
    plan_name = models.CharField(max_length=200)
    duration_months = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    status = models.IntegerField(choices=PLAN_STATUS, default=1)

    def __str__(self):
        return f"{self.plan_name} - {self.gym.gym_name}"
    
    class Meta:
        ordering = ['price']


MEMBERSHIP_STATUS = ((0, "Expired"), (1, "Active"), (2, "Cancelled"))

class Membership(models.Model):
    member = models.ForeignKey(
        'members.Member',  # ← STRING REFERENCE, not import
        on_delete=models.CASCADE, 
        related_name="memberships"
    )
    membership_plan = models.ForeignKey(
        MembershipPlan, on_delete=models.PROTECT, related_name="memberships"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.IntegerField(choices=MEMBERSHIP_STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.first_name} - {self.membership_plan.plan_name}"
    
    class Meta:
        ordering = ['-start_date']
