from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('registration',views.Userregestration,name='registration'),
    path('sample',views.sample,name='sample'),
    path('login',views.loginpage,name='loginpage'),
    path('logout',views.logout,name='logout'),
    path('team',views.team,name='team'),
]