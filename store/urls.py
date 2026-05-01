from django.urls import path
from . import views

urlpatterns = [
    # 🏠 HOME
    path('', views.home, name='home'),

    # 👤 AUTH
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account_dashboard, name='account'),

    # 🛒 CART
    path('cart/', views.cart, name='cart'),

    # 🛍️ PRODUCTS
    path('products/', views.product_list, name='products'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),

    # ➕ PRODUCT MANAGEMENT
    path('create/', views.product_create, name='product_create'),
]