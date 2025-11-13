from django.db import models
from members.models import Member
from memberships.models import Membership

# Create your models here.

PAYMENT_STATUS = ((0, "Pending"), (1, "Completed"), (2, "Failed"))

class Payment(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.SET_NULL, null=True, related_name="payments"
    )
    membership = models.ForeignKey(
        Membership, on_delete=models.SET_NULL, null=True, related_name="payments"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    status = models.IntegerField(choices=PAYMENT_STATUS, default=1)

    def __str__(self):
        return f"{self.member.first_name if self.member else 'Unknown'} - £{self.amount}"

    class Meta:
        ordering = ['-payment_date']
