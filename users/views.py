from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import User
from doctors.models import Doctor
from appointment.models import Appointment
from .froms import UserRegistrationForm

# Create your views here.

def index(request):
    return render(request, 'home/home.html', {'doctors': Doctor.objects.filter(id__range=(1, 4))})


def register(request):
    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)


        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        if user is not None and user.check_password(password):
            auth_login(request, user)  # Вставляем auth_login, чтобы использовать встроенную функцию
            messages.success(request, 'Welcome back!')
            return redirect('index')  # Перенаправление на главную страницу после входа
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'users/login.html')



def paswd_reset(request):
    return render(request, 'home/home.html')


def schedules(request):
    return render(request, 'home/schedules.html', {'appointments': Appointment.objects.all})