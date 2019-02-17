#django imports
from django.shortcuts import render
from django.http import HttpResponse


def signUp(request):
    return HttpResponse("Hello world. you are at the the polls index")

def signUpResult(request, name):
    response = "You have registered successfully as"
    return HttpResponse(response % name)
