from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Перенаправление на страницу успешной записи
    else:
        form = AppointmentForm()

    return render(request, 'appointment/appointment.html', {'form': form})



def success(request):
    return render(request, 'appointment/success.html')