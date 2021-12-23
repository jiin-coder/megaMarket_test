from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from products.models import Product
from questions.models import Question

def create_question(request: HttpRequest, content_type, object_id):
    product_id = object_id
    if content_type == "product":
        product = Product.objects.get(id=product_id)
        product_content_type = ContentType.objects.get_for_model(product)
        body = request.POST.get("body")
        question = Question(user_id=1, content_type=product_content_type, object_id=product_id, body=body)
        question.save()
        return redirect("products:detail", id=product_id)
    return HttpResponse("성공")

