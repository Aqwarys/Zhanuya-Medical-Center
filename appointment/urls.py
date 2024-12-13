from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_appointment, name='appointment'),
    path('success/', views.success, name='success')
]
