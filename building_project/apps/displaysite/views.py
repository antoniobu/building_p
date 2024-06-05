from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib import messages
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
from .forms import UserForm

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
def login(request):
    return render(request, 'displaysite/login.html')

def contacts(request):
    return render(request, 'displaysite/contacts.html')

def signup(request):
    form = UserForm()
    data={'form':form}
    return render(request, 'displaysite/signup.html', data)

def cart(request):

    return render(request, 'displaysite/cart.html')