from django.shortcuts import render, redirect
from .models import Super, Power

def index(request):
    supers = Super.objects.all()
    context = {
        'supers': supers
    }
    return render(request, 'index.html', context)

def powers(request):
    powers = Power.objects.all()
    supers = Super.objects.all()
    context = {
        'powers': powers,
        'supers': supers
    }
    return render(request, 'powers.html', context)

def add_power(request):
    correct_super = Super.objects.get(id = request.POST['super_id'])
    power = Power.objects.create(
        ability = request.POST['ability']
    )
    power.supers.add(correct_super)
    return redirect('/powers')