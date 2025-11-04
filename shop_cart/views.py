from django.shortcuts import render, redirect, get_object_or_404
from shop_products.models import Product
from .models import Cart

def view_cart(request):
    items = Cart.objects.filter(user=request.user)
    return render(request, 'shop_cart/cart.html', {'items': items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def increase_quantity(request, item_id):
    item = get_object_or_404(Cart, id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('view_cart')

def decrease_quantity(request, item_id):
    item = get_object_or_404(Cart, id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('view_cart')

def checkout_view(request):
    items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in items)
    
    if request.method == "POST":
        items.delete()
        return redirect('thank_you')

    return render(request, "shop_cart/checkout.html", {
        "items": items,
        "total_price": total_price
    })

def thank_you_view(request):
    return render(request, "shop_cart/thank_you.html")
