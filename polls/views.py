#django imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

#project imports
from .models import Users

def users(request):
    users_list = Users.objects.all()
    output = ', '.join([u.username for u in users_list])
    return HttpResponse(output)

def signUpResult(request, name):
    response = "You have registered successfully as"
    return HttpResponse(response % name)

def signUp(request):
    return render(request, 'polls/signUp.html')

def submit_info(request):
    user = Users()
    user.username = request.POST.get('username','')
    user.email = request.POST.get('email','')
    user.password = request.POST.get('password','')
    user.repass = request.POST.get('repass','')
    user.save()
    return HttpResponse("OK")