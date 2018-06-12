from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.


def index(request):
    return render(request, "index.html", {"list": user_list})


user_list = [
    {"user": "admin", "pwd": "admin"},
    {"user": "user", "pwd": "pwd"}
]


def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        temp = {"user": username, "pwd": password}
        user_list.append(temp)
        print(username, password)
    return render(request, "index.html", {"list": user_list})
