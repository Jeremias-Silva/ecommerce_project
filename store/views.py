from django.shortcuts import render

def product_list(request):
    return render(request, 'base.html, products.html')# Create your views here.
