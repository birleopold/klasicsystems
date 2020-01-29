from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
import random



from products.models import Product, Service
from categories.models import Category

# Create your views here.



def home(request):
    products = Product.objects.order_by('?')[:9]
    categories = Category.objects.all()[:6]
    services = Service.objects.all()[:9]
    context = {
		'title': 'Home',
		'categories': categories,
		'products' : products,
        'services' : services
	}

    return render(request, 'home.html', context)


def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
		'title' : 'All Products',
		'products': products
	}
    return render(request,'all_products.html', context)

def all_services(request):
    services = Service.objects.all()
    paginator = Paginator(services, 9)
    page = request.GET.get('page')
    services = paginator.get_page(page)
    context = {
		'title' : 'All Services',
		'services': services
	}
    return render(request,'all_services.html', context)



def about(request):

    return render(request, 'about.html')



def product_by_slug(request,slug):
    product = Product.objects.get(slug=slug)
    if product.quantity >= 1:
        context = {
			'title' : product.title,
			'product': product
		}
        return render(request,'single.html',context)
    else:
        messages.warning(request,'Product is not Available')
        return redirect('pages:all_products')

def service_by_slug(request,slug):
    service = get_object_or_404(Service, slug = slug)
    #service = Service.objects.get(slug=slug)
    context = {
			'title' : service.title,
			'service': service
		}
    return render(request,'single_service.html',context)
   




def category_by_slug(request,slug):
    cat = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=cat.id)
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
		'title' : 'All Products',
		'products': products
	}
    return render(request,'all_products.html',context)





