from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        'time': strftime("%d-%m-%Y %H:%M, %A", gmtime())
    }
    return render(request, 'index.html', context)