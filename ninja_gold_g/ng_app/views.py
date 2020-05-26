from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'total' not in request.session or 'log' not in request.session:
        request.session['total'] = 0
        request.session['log'] = []
    return render(request,'index.html')

def process(request):
    if request.method == "POST":
        if request.POST['block'] == 'farm':
            gold = random.randint(10,21)
            request.session['log'].append('Yeah! You have earned '+ str(gold) + ' golds from ' + request.POST['block'] +'' + ' on ('+ str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['block'] == 'cave':
            gold = random.randint(5, 11)
            request.session['log'].append('Yeah! You have earned '+ str(gold) + ' golds from ' + request.POST['block'] +'' + ' on ('+ str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['block'] == 'house':
            gold = random.randint(2, 6)
            request.session['log'].append('Yes! You have earned '+ str(gold) + ' golds from ' + request.POST['block'] +'' + ' ('+ str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['block'] == 'casino':
            gold = random.randint(-50, 51)
            if gold >= 0:
                request.session['log'].append('You just earned '+ str(gold)+ ' golds ' +  ' ('+ str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        
            else:
                request.session['log'].append('Oh no! You lost '+ str(gold)+ ' golds ' + ' ('+ str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ') TRY AGAIN!')
                request.session['style'] = 'lost'
        
        request.session["total"] += gold

    return redirect('/')


def reset(request):
    if request.method =="POST":
        request.session['total'] = 0
        request.session['log'] = []
    return redirect('/')
