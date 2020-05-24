from django.shortcuts import render, redirect
import random

def index(request):
    if "feed" not in request.session:
        request.session['feed'] = []
    # if 'results' not in request.session:
        # request.session['results'] = []
    return render(request,'index.html');

def choice(request):
    print(request.method)
    if request.method =='POST':
        ran_num = int(random.random()*10)
        if int(request.POST['pick']) > ran_num:
            # request.session['results'].append(f"{request.POST['username']} guessed too high. {request.POST['pick']} was higher than {ran_num}")
            request.session['result'] ="You guessed too high"
            request.session['feed'].append( request.session['result'])
            request.session['style'] = 'high'
        elif int(request.POST['pick']) < ran_num:
            #  request.session['results'].append(f"{request.POST['username']} guessed too low .Guess: {request.POST['pick']} was lower than {ran_num}")
            request.session['result']="You guessed too low"
            request.session['feed'].append( request.session['result'])
            request.session['style'] = 'low'
        else:
            # request.session['results'].append(f"{request.POST['username']} guessed the number {ran_num}")
            request.session['result'] = "Bingo!"
            request.session['feed'].append( request.session['result'])
            request.session['style'] = 'bingo'
    
        print(ran_num, "This is the random number!")
        # print(request.POST,"This is my request.POST!")
        print(request.POST['pick'])
        print(request.session['results'])
        return redirect('/')
    return redirect('/')