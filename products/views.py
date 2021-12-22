from django.shortcuts import render, get_object_or_404
from .models import Product

def list(request):
    """
    pybo 목록 출력
    """
    product_list = Product.objects.order_by('-reg_date')
    context = {'product_list': product_list}
    return render(request, 'products/product_list.html', context)


def detail(request, product_id):
    """
    상품 상세 내용 출력
    """
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
