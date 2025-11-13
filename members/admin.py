from django.contrib import admin
from .models import Gym

class MemberInline(admin.TabularInline):
    from members.models import Member
    model = Member
    extra = 0
    readonly_fields = ['first_name', 'last_name', 'email', 'phone_number', 'status']
    can_delete = False

class GymAdmin(admin.ModelAdmin):
    inlines = [MemberInline]

admin.site.register(Gym, GymAdmin)
