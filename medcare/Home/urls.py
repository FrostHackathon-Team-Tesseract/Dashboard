
from django.urls import path
from .views import landingpage, login_view, register, home, bookAppointment, symptomChecker
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',landingpage,name='landingpage'),
    path('loginclient/',login_view,name='login'),
    path('registerclient/',register,name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('clienthome/',home,name='clienthome'),
    path('bookappointment/',bookAppointment, name='bookappointment'),
    path('symptomchecker/',symptomChecker,name='symptomchecker'),
]
