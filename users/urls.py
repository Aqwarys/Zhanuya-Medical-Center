from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('paswd_reset/', views.paswd_reset, name='paswd_reset'),
    path('schedules/', views.schedules, name='schedules')
]
