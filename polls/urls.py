#django imports
from django.urls import path

#project imports
from . import views
from .templates import polls


urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('signUpResult/', views.signUpResult, name='signUpResult'),
    path('submit_info/', views.submit_info, name='submit_info'),
    path('login/', views.login, name='login'),
]
