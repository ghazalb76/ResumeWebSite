#django imports
from django.shortcuts import render
from django.http import HttpResponse

#project imports
from .models import User

def users(request):
    users_list = User.objects.all()
    output = ', '.join([u.name for u in users_list])
    return HttpResponse(output)

def signUpResult(request, name):
    response = "You have registered successfully as"
    return HttpResponse(response % name)

def signUp(request):
    return render(request, 'polls/signUp.html')
