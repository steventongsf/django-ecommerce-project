from carts.views import _cart_id
from .models import Cart, CartItem


def counter(request):
    count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                count = count + cart_item.quantity
        except Cart.DoesNotExist:
            count = 0
    return dict(cart_count=count)
