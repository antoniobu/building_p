from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib import messages

from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
from django.db.models import Q
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the displaysite index.")
    products = Product.objects.prefetch_related('images').all()
   
    #products where discount > 0
    actionproducts = products.filter(discount__gt=0)
    return render(request, 'displaysite/index.html', {'products': products, 'actionproducts': actionproducts,'user': request.user},)

def product(request, product_id):
    product = Product.objects.prefetch_related('images').get(id=product_id)
    #write code to make an array with 4 products of the same category
    products = Product.objects.prefetch_related('images').filter(category=product.category)
    #delete current product from the array
    products = products.exclude(id=product_id)
    return render(request, 'displaysite/product.html', {'product': product, 'products': products})


def loyaltyprogram(request):
    return render(request, 'displaysite/loyaltyprogram.html')
#write a function for login
def login(request):
    #add login from form
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
    return render(request, 'displaysite/login.html')
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Пользователь аутентифицирован успешно, перенаправьте куда-нибудь
                return redirect('/displaysite')
    else:
        form = AuthenticationForm()
    return render(request, 'displaysite/login.html', {'form': form})
def contacts(request):
    return render(request, 'displaysite/contacts.html')
def myaccount(request):
    return render(request, 'displaysite/myaccount.html')
def signup(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Создаем пользователя
            user = User.objects.create_user(username=username)
            # Хешируем пароль
            user.set_password(password)
            user.save()
            
            return redirect('/displaysite')   
    else:
        error = 'Введено невірні дані, спробуйте ще раз'
    form = UserForm()
    data = {'form': form, 'error': error}
    return render(request, 'displaysite/signup.html', data)

def cart(request):

    return render(request, 'displaysite/cart.html')

def about(request):

    return render(request, 'displaysite/about.html')


def allproducts(request):
    sort_by = request.GET.get('sort', 'default')
    query = request.GET.get('q', '')

    products = Product.objects.prefetch_related('images')

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(brand__icontains=query)
        )

    if sort_by == 'alphabetical':
        products = products.order_by('name')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'brand':
        products = products.order_by('brand')
    else:
        products = products.all()

    return render(request, 'displaysite/allproducts.html', {'products': products, 'query': query, 'sort_by': sort_by})