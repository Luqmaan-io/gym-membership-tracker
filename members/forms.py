# members/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Member
from gym.models import Gym
from memberships.models import MembershipPlan

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'gym',
            'first_name', 
            'last_name', 
            'email', 
            'phone_number',
            'date_of_birth',
            'emergency_contact',
            'emergency_phone_number',
            'membership_plan',
            'status',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'emergency_contact': forms.Textarea(attrs={'rows': 2}),
        }
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get user from kwargs if provided
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'date_of_birth':
                field.widget.attrs['placeholder'] = 'YYYY-MM-DD'
        
        # Filter gyms to only those owned by the current user
        if user:
            self.fields['gym'].queryset = Gym.objects.filter(owner=user)
            # Filter plans to only those for the user's gym
            user_gym = Gym.objects.filter(owner=user).first()
            if user_gym:
                self.fields['membership_plan'].queryset = MembershipPlan.objects.filter(gym=user_gym, status=1)
    
    def clean_email(self):
        """Custom validation for email uniqueness"""
        email = self.cleaned_data.get('email')
        
        if self.instance and self.instance.pk:
            # Editing existing member
            existing = Member.objects.filter(email=email).exclude(pk=self.instance.pk).first()
        else:
            # Creating new member
            existing = Member.objects.filter(email=email).first()
            
        if existing:
            raise ValidationError(f'A member with email "{email}" already exists.')
        return email