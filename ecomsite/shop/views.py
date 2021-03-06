from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    products = Product.objects.all()

    # search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = Product.objects.filter(title__icontains=item_name)

    # pagination
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'shop/index.html', {'products': products})


def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product': product})


def checkout(request):

    if request.method == 'POST':
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")

        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode)
        order.save()

    return render(request, 'shop/checkout.html')


