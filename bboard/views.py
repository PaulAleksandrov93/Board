from django.http import HttpResponse# Создаем экземпляр класса HttpResponse
from .models import Bb

def index(request):#request - экземпляр класса HttpRequest
    s = 'Список объявлений \r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')#HttpResponse - отправляет строку в ответ на запрос-