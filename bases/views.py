from django.shortcuts import render 

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic 

class Home(LoginRequiredMixin, generic.Templateview):
tempate_name = 'Base/blank.html'
login_url='/admin'