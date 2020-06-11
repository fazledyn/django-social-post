from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages


@login_required
def dashboard(request):
    if request.method == 'POST':
        author          = request.user.username
        post_title      = request.POST.get("title")
        post_content    = request.POST.get("content")
        post_image      = request.FILES.get("postimage")

        print(post_image)

        new_post = Post.objects.create(title=post_title, content=post_content, image=post_image, author=author)
        new_post.save()

        return redirect('dashboard')

    else:

        post_list = Post.objects.all()
        context = {'post_list':post_list}

        return render(request, 'dashboard.html', context)


@login_required
def site_logout(request):
    logout(request)
    return redirect('index')


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        return redirect('signup')
        
    else:
        form = UserCreationForm()
        context = {'form': form}

        return render(request, 'signup.html', context)


def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("username: ", username, " password: ", password)
            return redirect('dashboard')

        return render(request, 'index.html')
    
    else:
        return render(request, 'index.html')
