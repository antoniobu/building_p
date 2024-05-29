from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the displaysite index.")
    all_products = Product.objects.all()
    return render(request, 'displaysite/index.html', {'all_products': all_products})