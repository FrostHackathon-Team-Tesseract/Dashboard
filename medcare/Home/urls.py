
from django.urls import path
from .views import landingpage, login, register

urlpatterns = [
    path('',landingpage,name='landingpage'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
]
