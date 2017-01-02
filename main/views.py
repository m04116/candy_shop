from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from main.models import *


def home(request):
    goods = Item.objects.all()
    context = {
        'title': 'Candy shop!',
        'goods': goods,
    }
    return HttpResponse(render_to_string('index.html', context))

def item(request, alias):
    try:
        good = Item.objects.get(alias=alias)
    except:
        return Http404
    context = {
        'good': good,
    }
    return HttpResponse(render_to_string('good.html', context))
