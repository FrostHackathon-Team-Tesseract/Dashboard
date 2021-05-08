from django.shortcuts import render, redirect
from .forms import Registrationform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Doctors
import requests


# Create your views here.
def landingpage(request):
    return render(request,'landing.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/clienthome')
   
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/clienthome')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "loginclient.html",
                    context={"form":form})
    


def register(request):
    if request.user.is_authenticated:
        return redirect('/clienthome')
    form = Registrationform()
    try:
        if request.method == 'POST':
            f = Registrationform(request.POST)
            print('in post')
            if f.is_valid(): 
                f.save()
                print('saved')
                username = f.cleaned_data.get('username')
                password = f.cleaned_data.get('password1')
                print(password)
                user = authenticate(username=username, password=password)
                login(request,user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/clienthome')
            else:
                messages.error(request, 'Password Did not match')

    except:
        messages.error(request, 'Invalid credentials')

    else:
        form = Registrationform()
    return render(request,'signupclient.html',{'form':form})


    

def home(request):
    return render(request,'home.html')



def bookAppointment(request):
    if request.method == 'POST':
        val = request.POST.get('btn')
        print(val)
    queryset = Doctors.objects.all()
    return render(request,'bookappointment.html',{'queryset':queryset})

#################################################################################

def symptomChecker(request):
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjFtczE4Y3MwODZAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiI5MDY1IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMjAwIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6Ijk5OTk5OTk5OSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IlByZW1pdW0iLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xhbmd1YWdlIjoiZW4tZ2IiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyMDk5LTEyLTMxIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwc3RhcnQiOiIyMDIxLTA1LTA3IiwiaXNzIjoiaHR0cHM6Ly9zYW5kYm94LWF1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE2MjA0NzU1OTUsIm5iZiI6MTYyMDQ2ODM5NX0.1GHFzRPimQjLEINNHiLcWngrShzqelTSp440uU_z4LM" 
    #token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjFtczE4Y3MwODZAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiI5MDY1IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMjAwIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6Ijk5OTk5OTk5OSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IlByZW1pdW0iLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xhbmd1YWdlIjoiZW4tZ2IiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyMDk5LTEyLTMxIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwc3RhcnQiOiIyMDIxLTA1LTA3IiwiaXNzIjoiaHR0cHM6Ly9zYW5kYm94LWF1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE2MjA0Njc5NDMsIm5iZiI6MTYyMDQ2MDc0M30.-yDPoaWH8BjmHX0FAfnb-zdtYySPXmPmm70aiy_Hm0s"
    if request.method == 'POST':
        val = request.POST.get('age')
        gender = request.POST.get('gender')
        res = requests.request("GET", f'https://sandbox-healthservice.priaid.ch/symptoms?token={token}&language=en-gb&format=json')
        data = res.json()
        symptoms = [[]]
        for d in data:
            symptoms.append([d['ID'],d['Name']])
        del(symptoms[0])
        return render(request, 'symptomchecker.html',{
        'age':False,
        'symptom':True,
        'diagnosis':False,
        'issue':False,
        'symptoms':symptoms

    })
    
   
    return render(request,'symptomchecker.html', {
        'age':True,
        'symptom':True,
        'diagnosis':False,
        'issue':False,
    })