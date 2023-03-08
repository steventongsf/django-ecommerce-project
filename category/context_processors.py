from .models import Category
def menu_links(request):
    links = Category.objects.all()
    print("links:",type(links))
    return dict(links=links)