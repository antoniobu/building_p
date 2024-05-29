from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the displaysite index.")
    all_products = Product.objects.prefetch_related('images').all()
    return render(request, 'displaysite/index.html', {'all_products': all_products})

def product(request, product_id):
    product = Product.objects.prefetch_related('images').get(id=product_id)
    return render(request, 'displaysite/product.html', {'product': product})