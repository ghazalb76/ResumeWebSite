#django imports
from django.urls import path

#project imports
from . import views


urlpatterns = [
    path('signUp/', views.index, name='signUp')
    path('signUpResult', views.signUpResult, name='signUpResult')
]
