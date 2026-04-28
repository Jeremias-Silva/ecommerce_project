from django.shortcuts import render

def product_list(request):
    return render(request, 'base.html')# Create your views here.
    return render(request, 'products.html')# Create your views here.