from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse

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
            return redirect('home')  # Redirect to homepage after login
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    # If GET request or failed login, show the login form
    return render(request, 'members/login.html')