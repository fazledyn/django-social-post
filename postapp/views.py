from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


# sub-function for creating posts
def create_post(request):
    author = request.user.username
    post_title = request.POST.get("title")
    post_content = request.POST.get("content")
    post_image = request.FILES.get("postimage")

    new_post = Post.objects.create(title=post_title,
                                   content=post_content,
                                   image=post_image,
                                   author=author)
    new_post.save()


@login_required
def dashboard(request):
    if request.method == 'POST':
        create_post(request)
        return redirect('dashboard')

    else:
        post_list = Post.objects.all()
        context = {'post_list': post_list}

        return render(request, 'dashboard.html', context)


@login_required
def site_logout(request):
    logout(request)
    return redirect('index')


def signup(request):
    error_messages = []

    if request.method == 'POST':
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2 and len(password1) >= 8:
            new_user = User.objects.create_user(
                username=username, password=password1)
            new_user.save()
            print("new user creatd !")
            return redirect('/')

        if username == password1:
            error_messages.append("Username and password can't be same !")

        if len(password1) < 8:
            error_messages.append("Passwords must be 8 character long")

        if password1 != password2:
            error_messages.append("Passwords don't match !")

        if User.objects.filter(username=username) is None:
            error_messages.append("User already exists !")

    context = {'errors': error_messages}
    return render(request, 'signup.html', context)


def index(request):

    if request.session.get('user_name', "Anonymous") is not "Anonymous":
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['user_name'] = username
            print("username: ", username, " password: ", password)
            return redirect('dashboard')

    return render(request, 'index.html')
