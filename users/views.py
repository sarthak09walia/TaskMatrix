from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegistrationForm
from .models import CustomUser 


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            # Check if passwords match
            if password1 == password2:
                # Create a new user
                user = CustomUser.objects.create_user(username=username, password=password1)
                login(request, user)
                messages.success(request, f'Account created successfully. Welcome, {username.title()}!')
                return redirect('Tasks')
            else:
                messages.error(request, 'Passwords do not match.')
    else:
        form = RegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})

def sign_in(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('Tasks')
        
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('Tasks')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})
    
def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login') 

