from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from apparelstore import settings
from carts.models import CartItem
from carts.views import _cart_id

from category.models import Category

from store.models import Product, Variation, VariationManager

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    links = Category.objects.all()
    # fetch data from database, create context and pass to template
    print("request")
    if category_slug is not None:
        print("category_slug: ", category_slug)
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        "products": products,
        "links": links, 
        "product_count": product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    #print("category_slug, product_slug: ", category_slug, product_slug)
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        # VariationManager not working so explicitly getting variations and passing to context
        product_colors = Variation.objects.filter(product_id=single_product.id,variation_category="color")
        product_sizes = Variation.objects.filter(product_id=single_product.id,variation_category="size")
        is_in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        for s in product_sizes:
            print("product_size: ",s.variation_value)
        # if settings.DEBUG:
        #     return HttpResponse("Is in cart: "+str(is_in_cart))
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'product_colors':product_colors,
        'product_sizes':product_sizes,
        'is_in_cart': is_in_cart,
    }
    return render(request, "store/product-detail.html", context)