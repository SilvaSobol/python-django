from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("HELLO THERE!")

# Create your views here.
