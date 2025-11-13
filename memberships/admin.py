from django.contrib import admin
from .models import MembershipPlan, Membership

# Register your models here.
admin.site.register(MembershipPlan)
admin.site.register(Membership)
