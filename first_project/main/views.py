from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
import datetime

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import Group


# Create your views here.

def index_view(request):
    context = {
        'date': datetime.datetime.now(),
        'range': range(1,11)}
    return render(request, 'main/index.html', context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'main/sign-up.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        hr_group, created = Group.objects.get_or_create(name = 'HR')
        self.object.groups.add(hr_group)


        login(self.request,self.object)
        return response

class CustomSignInView(LoginView):
    template_name = 'main/sign-in.html'

