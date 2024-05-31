from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the displaysite index.")
    products = Product.objects.prefetch_related('images').all()
    return render(request, 'displaysite/index.html', {'products': products})

def product(request, product_id):
    product = Product.objects.prefetch_related('images').get(id=product_id)
    #write code to make an array with 4 products of the same category
    products = Product.objects.prefetch_related('images').filter(category=product.category)
    #delete current product from the array
    products = products.exclude(id=product_id)
    return render(request, 'displaysite/product.html', {'product': product, 'products': products})


def loyaltyprogram(request):
    return render(request, 'displaysite/loyaltyprogram.html')