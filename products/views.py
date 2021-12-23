from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Product

def list(request: HttpRequest): # 상품 목록
    product_list = Product.objects.order_by('-reg_date')

    return render(request, 'products/product_list.html', {
      "product_list": product_list
    })


def detail(request: HttpRequest, product_id): # 상세 화면
    product = get_object_or_404(Product, id=product_id)

    return render(request, "products/product_detail.html", {
        "product": product
    })

