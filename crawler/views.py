from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import datetime
from crawler import models


# Create your views here.


def index(request):
    return render(request, "index.html", {"list": models.UserInfo.objects.all()})


user_list = [
    {"user": "admin", "pwd": "admin"},
    {"user": "user", "pwd": "pwd"}
]


def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(user=username, pwd=password, bpub_date=datetime.datetime.now())
        print(username, password)
    # return render(request, "index.html", {"list": models.UserInfo.objects.all()})
    return redirect('/index/')
