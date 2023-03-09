from django.shortcuts import render

from .models import Bb

def index(request):#request - экземпляр класса HttpRequest
    bbs = Bb.objects.order_by('-published')
    return render (request, 'bboard/index.html', {'bbs': bbs})#HttpResponse - отправляет строку в ответ на запрос-