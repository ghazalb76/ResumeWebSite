#django imports
from django.urls import path

#project imports
from . import views


urlpatterns = [
    path('users/', views.users, name='users'),
    path('signUp/', views.signUp, name='signUp'),
    path('signUpResult/', views.signUpResult, name='signUpResult'),
]
