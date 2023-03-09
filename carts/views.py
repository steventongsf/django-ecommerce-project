from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from carts import views
from carts.models import Cart, CartItem
from store.models import Product
from django.shortcuts import render,redirect

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart 
def add_cart(request, product_id):
    # get existing product
    product = Product.objects.all().get(id=product_id)
    # make sure there is a cart by session id
    try:
        # cookie.sessionid
        cart = Cart.objects.all().get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request))
    cart.save()
    try:
        # get cart item
        cart_item = CartItem.objects.get(product=product,cart=cart)
        # increment quantity
        cart_item.quantity += 1
    except CartItem.DoesNotExist:
        # create cart item
        cart_item = CartItem.objects.create(product=product, quantity=1, cart= cart)
    cart_item.save()
    #return HttpResponse(cart_item)
    return redirect('cart')

def cart(request,total=0,quantity=0,cart_tems=None):
    try:
        cart =  Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = ( 2 * total / 100 )
        grand_total = total + tax
    except Cart.DoesNotExist:
        return render(request,"store/store.html", context)
    context = {
        "total": total,
        "quantity": quantity,
        "cart_items": cart_items,
        "grand_total": grand_total,
        "tax": tax,

    }
    return render(request,"store/cart.html", context)

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()    
    else:
        cart_item.delete()
    
    return redirect('cart')



def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    
    return redirect('cart')

def checkout():
    pass