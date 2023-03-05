from django.http import HttpResponse# Создаем экземпляр класса HttpResponse

def index(request):#request - экземпляр класса HttpRequest
    return HttpResponse("Здесть будет выведен список объявлений.")#HttpResponse - отправляет строку в ответ на запрос