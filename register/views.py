from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # authenticate user and log them in
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})