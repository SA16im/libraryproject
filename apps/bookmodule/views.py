from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'bookmodule/index.html')

def viewbook(request, bookId):
    return HttpResponse(f"Displaying book with ID: {bookId}")

def welcome(request):
    return HttpResponse("Welcome to our Library!")