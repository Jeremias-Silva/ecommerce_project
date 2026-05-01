from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm, RegisterForm


# 🏠 HOME
def home(request):
    return render(request, "store/home.html")


# 👤 REGISTER
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = RegisterForm()

    return render(request, 'store/register.html', {'form': form})


# 🔐 LOGIN (FUNCIONAL + REDIRECT PARA DASHBOARD)
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/account/')  # 👈 dashboard
        else:
            return render(request, "login.html", {
                "error": "Invalid credentials"
            })

    return render(request, "login.html")


# 👤 DASHBOARD (ACCOUNT)
@login_required
def account_dashboard(request):
    return render(request, 'store/account.html')


# 🛒 PRODUCT LIST
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})


# ➕ CREATE PRODUCT
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'products/form.html', {'form': form})


# ✏️ UPDATE PRODUCT
def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'products/form.html', {'form': form})


# ❌ DELETE PRODUCT
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products')


# 📦 PRODUCT DETAIL
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/detail.html', {'product': product})


# 🛒 CART
def cart(request):
    return render(request, "cart.html")