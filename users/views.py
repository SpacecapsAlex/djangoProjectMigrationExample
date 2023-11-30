from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import User

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Response from django")


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("About page")


def welcome(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('response.html')
    return HttpResponse(template.render())


def register(request: HttpRequest) -> HttpResponse:
    try:
        user = User(name='Alex', age=20)  # Создание объекта класса User
        user.save()  # Сохранение объекта класса User в базе данных!!!!!!!!!!!
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")


def get_users(request: HttpRequest) -> HttpResponse:
    users = User.objects.all().values()  # Получение всех объектов класса User из базы данных
    return HttpResponse(users)

# Удаление
# 1) Получить объект
# 2) Удалить объект(полученный)
def delete_user(request: HttpRequest) -> HttpResponse:
    try:
        user = User.objects.get(id=1)  # Получение объекта класса User из базы данных по id
        user.delete()  # Удаление объекта класса User из базы данных по id(удаление объекта полученного в строчке 38)
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")


def update_user(request: HttpRequest) -> HttpResponse:
    try:
        user = User.objects.get(id=1)  # Получение объекта класса User из базы данных по id
        user.name = 'Alex'  # Изменение имени объекта класса User
        # user.id = 1  # Изменение id объекта класса User(При изменении id объекта класса User на несуществующий в базе, создаётся новая запись)
        user.save()  # Сохранение объекта класса User в базе данных!!!!!!!!(Изменение, т.к. запись с id=1 присутствует)
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")


def test_template(request: HttpRequest) -> HttpResponse:
    user = User.objects.get(id=2)
    template = loader.get_template('test.html')
    data = {
        'header': user.name,
        'phrase': user.age,
    }
    return HttpResponse(template.render(data))


def list_requests(request: HttpRequest) -> HttpResponse:
    users = User.objects.all().values()
    template = loader.get_template('list_example.html')
    data = {
        'header': 'Пользователи',
        'users': users,
    }
    return HttpResponse(template.render(data))


def get_user_profile(request: HttpRequest, id: int) -> HttpResponse:
    try:
        user = User.objects.get(id=id)
        template = loader.get_template('user_profile.html')
        data = {
            'header': 'Профиль пользователя',
            'user': user,
        }
        return HttpResponse(template.render(data, request))
    except:
        return HttpResponse("Error")
