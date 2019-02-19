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

def login(request):
    user_name = request.POST.get('user_name','')
    password = request.POST.get('pass_word','')
    users_list = Users.objects.all()
    print (user_name)
    print (password)
    for user in users_list:
        print (user.username)
        print (user.password)
        print("****")
        if user.username == user_name and user.password == password:
            return HttpResponse("Done")
    return HttpResponse("User does not exist")