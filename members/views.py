from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.http import HttpResponse
from .models import Member, MEMBER_STATUS
from gym.models import Gym 
from memberships.models import MembershipPlan
from .forms import MemberForm 

def members(request):
    return HttpResponse("Members page coming soon!")

def custom_login(request):
    # If user is already logged in, redirect them
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to homepage
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login the user
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            
            # Smart redirect: admins go to admin panel, gym owners go to dashboard
            if user.is_staff or user.is_superuser:
                return redirect('/admin/')  # Admin users go to Django admin
            else:
                return redirect('members:dashboard')  # Gym owners go to dashboard
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    # If GET request or failed login, show the login form
    return render(request, 'members/login.html')

def dashboard(request):
    return render(request, 'members/dashboard.html')



# === Gym owner - member CRUD views ===

@login_required
def member_list(request):
    """Display all members for the logged-in gym owner"""
    # Get the gym owned by the current user
    # Assuming each user has one gym they own
    gym = get_object_or_404(Gym, owner=request.user)
    members = Member.objects.filter(gym=gym)
    
    context = {
        'members': members,
        'gym': gym,
    }
    return render(request, 'members/member_list.html', context)

@login_required
def member_create(request):
    """Create a new member"""
    gym = get_object_or_404(Gym, owner=request.user)
    
    if request.method == 'POST':
        # Create form with POST data and user context
        form = MemberForm(request.POST, user=request.user)
        if form.is_valid():
            member = form.save()
            messages.success(request, f'Member {member.first_name} {member.last_name} added successfully!')
            return redirect('members:member_list')
        else:
            # Validation errors
            messages.error(request, 'Please correct the errors below.')
    else:
        # Create empty form for GET request
        form = MemberForm(user=request.user)
        # Pre-select the user's gym
        form.initial['gym'] = gym
    
    # If GET request or form invalid, show the form
    context = {
        'form': form,
        'title': 'Create New Member',
        'is_create': True,
    }
    return render(request, 'members/member_form.html', context)

@login_required
def member_update(request, member_id):
    """Update an existing member"""
    gym = get_object_or_404(Gym, owner=request.user)
    member = get_object_or_404(Member, id=member_id, gym=gym)
    
    if request.method == 'POST':
        # Update form with POST data, instance, and user
        form = MemberForm(request.POST, instance=member, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member {member.first_name} {member.last_name} updated successfully!')
            return redirect('members:member_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Pre-fill form with member data
        form = MemberForm(instance=member, user=request.user)
    
    # Show form for GET or invalid POST
    context = {
        'form': form,
        'member': member,
        'title': f'Edit Member: {member.first_name} {member.last_name}',
        'is_update': True,
    }
    return render(request, 'members/member_form.html', context)

@login_required
def member_delete(request, member_id):
    """Delete a member"""
    gym = get_object_or_404(Gym, owner=request.user)
    member = get_object_or_404(Member, id=member_id, gym=gym)
    
    if request.method == 'POST':
        member_name = f"{member.first_name} {member.last_name}"
        member.delete()
        messages.success(request, f'Member {member_name} deleted successfully!')
        return redirect('members:member_list')
    
    # If GET request, show confirmation page
    context = {
        'member': member,
        'gym': gym,
    }
    return render(request, 'members/member_confirm_delete.html', context)

@login_required
def member_detail(request, member_id):
    """View member details"""
    gym = get_object_or_404(Gym, owner=request.user)
    member = get_object_or_404(Member, id=member_id, gym=gym)
    
    context = {
        'member': member,
        'gym': gym,
        'status_choices': MEMBER_STATUS,
    }
    return render(request, 'members/member_detail.html', context)