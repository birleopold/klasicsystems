from django.shortcuts import render
from products.models import Product, service

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    services = Service.objects.filter(name__icontains=request.GET['q'])
    context = {
        "products": products
        "services": services
        }
    return render(request, "serarch.html", context)