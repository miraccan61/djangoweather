# this is my views

from django.shortcuts import render
from .api import *


def home(request):

    
    
    context={
        'timezone':timezone,
        'city_name':city_name,
        'country_code':country_code,
        'app_temp':app_temp,
        'icon':icon,
        'description':description,
        'day':day,
        'month':month,
        'year':year
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {})
