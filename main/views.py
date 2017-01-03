from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from main.models import *


def home(request):
    category = Category.objects.all()
    context = {
        'sitename': 'Candy shop!',
        'categories': category,
    }
    return HttpResponse(render_to_string('home.html', context))


def item(request, alias):
    try:
        good = Item.objects.get(alias=alias)
    except:
        raise Http404('Товар не найден')
    context = {
        'good': good,
    }
    return HttpResponse(render_to_string('good.html', context))


def get_category(request, alias):
    try:
        category = Category.objects.get(alias=alias)
        goods = Item.objects.filter(category=category)
    except:
        raise Http404('Товары не найдены')
    context = {
        'goods': goods,
        'category': category,
    }
    return HttpResponse(render_to_string('index.html', context))
