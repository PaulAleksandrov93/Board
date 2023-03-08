from django.http import HttpResponse# Создаем экземпляр класса HttpResponse
from django.template import loader

from .models import Bb

def index(request):#request - экземпляр класса HttpRequest
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))#HttpResponse - отправляет строку в ответ на запрос-