
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here


def index(request):
    #return HttpResponse("Hello, Welcome to my profile") 


    return render(request, 'maj_profile/index.html')