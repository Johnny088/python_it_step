from django.shortcuts import render

import random

import datetime

# Create your views here.

def index_view(request):
    predictions = [
        "Today is the perfect day to learn something new in Django!",
        "An unexpected but pleasant meeting awaits you.",
        "Your persistence will bring great results very soon.",
        "Today is a great day to take a break from code and go for a walk.",
        "Focus on what's important, and all the small problems will solve themselves.",
        "Your coffee will be especially tasty today, and your code will be bug-free.",
        "Trust your intuition—it won't let you down.",
        "Today you will find the answer to a question that has been bothering you for a long time.",
        "Time for bold decisions. Take the first step!",
        "Remember: even the most complex task can be broken down into simple steps."
    ]
    context = {'date': datetime.datetime.now(), 'predictions': random.choice(predictions)}
    return render(request, 'main/index.html', context)