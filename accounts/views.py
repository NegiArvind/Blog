from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login') # after successful submission of signup form it will redirect to login page.
    template_name='sign_up.html'
