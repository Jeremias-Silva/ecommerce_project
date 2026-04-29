from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('login/', views.login_view, name='login'),
    path('cart/', views.cart, name='cart'),
]