from django.shortcuts import render, redirect
from .forms import Registrationform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


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