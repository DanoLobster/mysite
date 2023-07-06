from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists.')
            else:
                form.save()
                return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')