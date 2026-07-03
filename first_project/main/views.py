from django.shortcuts import render
import datetime
# Create your views here.

def index_view(request):
    context = {
        'date': datetime.datetime.now(),
        'range': range(1,11)}
    return render(request, 'main/index.html', context)