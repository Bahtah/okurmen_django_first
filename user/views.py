from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        user_date = {
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "email": request.POST.get("email"),
            "age": request.POST.get("age")
        }
        return render(request, 'user/index.html', {'title': 'Главная страница сайта', 'user_date': user_date})
        # first_name = request.POST.get("first_name")
        # last_name = request.POST.get("last_name")
        # email = request.POST.get("email")
        # age = request.POST.get("age")
        # return HttpResponse(f"<h2>Привет, {first_name} {last_name}, email: {email} твой возраст: {age}</h2>")
    else:
        userform = UserForm()
        return render(request, 'user/index.html', {'title': 'Главная страница сайта', 'form': userform})


def about(request):
    return render(request, 'user/about.html', {'title': 'Страница про нас'})
