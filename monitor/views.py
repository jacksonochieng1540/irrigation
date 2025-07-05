from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.shortcuts import render, redirect
from .models import SensorData
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    ...


def simulate_data():
    return {
        'soil_moisture': random.randint(30, 80),
        'water_level': random.randint(40, 100)
    }

def dashboard(request):
    data = simulate_data()
    last = SensorData.objects.last()
    status = last.irrigation_status if last else "OFF"

    SensorData.objects.create(
        soil_moisture=data['soil_moisture'],
        water_level=data['water_level'],
        irrigation_status=status
    )

    # Get last 10 entries
    history = SensorData.objects.order_by('-timestamp')[:10][::-1]

    timestamps = [DateFormat(h.timestamp).format('H:i') for h in history]
    moistures = [h.soil_moisture for h in history]
    water_levels = [h.water_level for h in history]

    context = {
        'soil_moisture': data['soil_moisture'],
        'water_level': data['water_level'],
        'irrigation_status': status,
        'timestamps': timestamps,
        'moistures': moistures,
        'water_levels': water_levels
    }
    return render(request, 'dashboard.html', context)


def toggle_irrigation(request):
    last = SensorData.objects.last()
    new_status = "OFF" if last and last.irrigation_status == "ON" else "ON"

    SensorData.objects.create(
        soil_moisture=last.soil_moisture,
        water_level=last.water_level,
        irrigation_status=new_status
    )
    return redirect('dashboard')