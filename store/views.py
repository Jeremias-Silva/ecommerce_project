from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# READ (listar)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

# CREATE
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'products/form.html', {'form': form})

# UPDATE
def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'products/form.html', {'form': form})

# DELETE
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products')

def product_list(request):
    return render(request, 'products.html')

def home(request):
    return render(request, 'store/home.html')

from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def products(request):
    return render(request, "products.html")

def login_view(request):
    return render(request, "login.html")

def cart(request):
    return render(request, "cart.html")