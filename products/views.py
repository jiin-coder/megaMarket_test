from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Product

def list(request: HttpRequest): # 상품 목록
    products = Product.objects.order_by('-reg_date')

    return render(request, 'products/product_list.html', {
      "products": products
    })


def detail(request: HttpRequest, product_id): # 상세 화면
    product = get_object_or_404(Product, id=product_id)

    product_reals = product.product_reals.order_by('option_1_display_name')
    return render(request, "products/product_detail.html", {
        "product": product,
        "product_reals": product_reals,
    })

