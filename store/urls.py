from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='products'),
    path('login/', views.login_view, name='login'),
    path('cart/', views.cart, name='cart'),
    path('create/', views.product_create, name='product_create'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]



