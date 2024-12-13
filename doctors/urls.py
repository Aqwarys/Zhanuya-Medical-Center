from django.urls import path
from . import views


app_name = 'doctors'
urlpatterns = [
    path('', views.sheet, name='sheet'),
    path('<int:doctor_id>', views.doctor, name='doctor')
]
