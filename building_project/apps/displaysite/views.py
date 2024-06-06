from django.shortcuts import render, redirect
from django.contrib.auth import login as login_func, logout
from django.contrib.auth import  authenticate
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.hashers import make_password


from .models import *
from .forms import *


# MAIN PAGE
def index(request):
    products = Product.objects.prefetch_related('images').all()
    actionproducts = products.filter(discount__gt=0)
    return render(request, 'displaysite/index.html', {'products': products, 'actionproducts': actionproducts,'user': request.user},)

#PRODUCT PAGE
def product(request, product_id):
    product = Product.objects.prefetch_related('images').get(id=product_id)
    products = Product.objects.prefetch_related('images').filter(category=product.category)
    products = products.exclude(id=product_id)
    return render(request, 'displaysite/product.html', {'product': product, 'products': products})

#LOYALTY PROGRAM PAGE
def loyaltyprogram(request):
    return render(request, 'displaysite/loyaltyprogram.html')

#CONTACTS PAGE
def contacts(request):
    return render(request, 'displaysite/contacts.html')

#MY ACCOUNT PAGE
def myaccount(request):
    orders = Order.objects.filter(user=request.user)
    orderitems = OrderItem.objects.filter(order__user=request.user)
    products = Product.objects.prefetch_related('images').all()
    return render(request, 'displaysite/myaccount.html', { 'products': products,'orders' : orders, 'orderitems' : orderitems})

#CART PAGE
def cart(request):
    return render(request, 'displaysite/cart.html')

#ABOUT PAGE
def about(request):

    return render(request, 'displaysite/about.html')

#ALL PRODUCTS PAGE(CATALOG)
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

#SIGNUP PAGE(MAKE A NEW ACCOUNT)
def signup(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Создаем объект пользователя, но пока не сохраняем его в базу данных
            user = form.save(commit=False)
            # Шифруем пароль
            user.password = make_password(form.cleaned_data['password'])
            # Сохраняем пользователя в базу данных
            user.save()
            return redirect('/displaysite')   
        else:
            error = 'Введено невірні дані, спробуйте ще раз'
            
            
    form = UserForm()
    data = {'form': form, 'error': error}
    return render(request, 'displaysite/signup.html', data)

#LOGIN PAGE
def login(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login_func(request, user)
                    return redirect('/displaysite')  
                else:
                    error = 'Введено невірні дані, спробуйте ще раз'
            else:
                error = 'Введено невірні дані, спробуйте ще раз'
        else:
             error = 'Введено невірні дані, спробуйте ще раз'
    form = LoginForm()
    data = {'form': form, 'error': error}
    return render(request, 'displaysite/login.html', data)

def logout_view(request):
    logout(request)
    return redirect('/displaysite')  