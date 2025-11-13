from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def attendance(request):
    return HttpResponse("This is the attendance page.")