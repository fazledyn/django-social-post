from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def site_logout(request):
    logout(request)
    return redirect('index')


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        
        return render(request, 'dashboard.html')
        
    else:
        form = UserCreationForm()
        context = {'form': form}

        return render(request, 'signup.html', context)


def site_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("username: ", username, " password: ", password)
            return redirect('dashboard')

        return render(request, 'login.html')
    
    else:
        return render(request, 'login.html')