from pickle import FLOAT
from token import NAME, STRING
from django.shortcuts import render
from django.http import HttpResponse
from .data import *

# импорт функции reverse для создания URL-адресов





def landing(request):
    """Главная страница сайта - лендинг"""
    context = {
        "title": "Барбершоп - стрижки и бритье",
        "masters": masters[:3],  # Показываем только первые 3 мастера
        "services": services,
    }
    return render(request, "landing.html", context)


def orders_list(request):
    context = {
        "orders": orders,
        "title": "Список заявок",
    }
    return render(request, "orders_list.html", context)


def index(request):
    # Перенаправляем на лендинг
    return landing(request)

def thanks(request):
    return render(request, "thanks.html")
