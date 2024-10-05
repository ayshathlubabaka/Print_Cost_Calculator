from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('user_dashboard/',views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/',views.admin_dashboard, name='admin_dashboard'),
    path('superuser_dashboard/',views.superuser_dashboard, name='superuser_dashboard'),
]