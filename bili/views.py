from django.shortcuts import render, HttpResponse


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "root" and password == "abc123":
            return HttpResponse("success")
        else:
            return HttpResponse("fail")
