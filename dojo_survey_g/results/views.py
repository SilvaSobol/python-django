from django.shortcuts import render, redirect

def index(request):
    return render(request,'survey.html')

def display(request):
    if request.method == 'POST':
        context = {
            "name": request.POST["name"],
            "loc": request.POST['location'],
            "lan": request.POST['language'],
            "com": request.POST['comments'],
            # "gen": request.POST['gender'],
            "how": request.POST['how']
        }
        return render(request,'output.html', context)
    return render(request,'output.html')



