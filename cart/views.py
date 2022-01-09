from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

# Create your views here.
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from cart.forms import ProductCartAddForm
from products.models import ProductReal

from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST, require_GET
from cart.models import CartItem

@login_required
@require_POST
def add(request: HttpRequest):
    product_real: ProductReal = ProductReal.objects.get(id=request.POST.get('product_real'))
    form = ProductCartAddForm(request.POST)

    if form.is_valid():
        cart_item = form.save(commit=False)
        cart_item.user = request.user
        cart_item.save()

        messages.success(request, "장바구니에 추가되었습니다.")
        return redirect('products:detail', product_real.product.id)

    messages.error(request, form['quantity'].errors, 'danger')
    return redirect('products:detail', product_real.product.id)


@login_required
@require_GET
def list(request: HttpRequest):
    cart_items = CartItem.objects.filter(user=request.user)

    return render(request, "cart/list.html", {
        "cart_items": cart_items
    })