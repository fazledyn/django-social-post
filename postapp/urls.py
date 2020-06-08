from django.urls import path
from . import views, admin

urlpatterns = [
    path('',            views.index,        name='index'),
    path('dashboard/',  views.dashboard,    name='dashboard'),
    path('login/',      views.site_login,   name='login'),
    path('signup/',     views.signup,       name='signup'),
    path('logout/',     views.site_logout,  name='logout'),
]