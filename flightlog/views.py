from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FlightLog
from .forms import FlightLogForm

@login_required
def log_list(request):
    logs = FlightLog.objects.filter(user=request.user).order_by('-date')
    return render(request, 'flightlog/log_list.html', {'logs': logs})

@login_required
def add_log(request):
    if request.method == 'POST':
        form = FlightLogForm(request.POST, request.FILES)
        if form.is_valid():
            flight_log = form.save(commit=False)
            flight_log.user = request.user
            flight_log.save()
            return redirect('log_list')
    else:
        form = FlightLogForm()
    return render(request, 'flightlog/add_log.html', {'form': form})
