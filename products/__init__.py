from django.http import HttpRequest

def product_list(request:HttpRequest):
    return HttpRequest("안녕")