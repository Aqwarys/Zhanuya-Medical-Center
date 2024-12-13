from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor

# Create your views here.
def sheet(request):
    return render(request, 'doctors/doctors.html', {'doctors': Doctor.objects.all})



def doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'doctors/doctor.html', {'doctor': doctor})