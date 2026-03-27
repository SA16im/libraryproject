from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # هذه الوظيفة ترسل نصاً بسيطاً للمتصفح
    return HttpResponse("Welcome to my library website!")