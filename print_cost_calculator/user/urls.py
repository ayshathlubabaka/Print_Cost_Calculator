from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('dashboard/',views.dashboard, name='dashboard'),
]