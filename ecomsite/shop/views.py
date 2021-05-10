from django.shortcuts import render
from .models import Product
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
    return render(request, 'shop/checkout.html')
