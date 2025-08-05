from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Home and product pages
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    
    # Cart functionality
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('update-cart-item/', views.update_cart_item, name='update_cart_item'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    
    # Checkout and orders
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/<str:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('orders/', views.order_history, name='order_history'),
    path('order/<str:order_id>/', views.order_detail, name='order_detail'),
    
    # User authentication and profile
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
    # Reviews
    path('product/<int:product_id>/review/', views.add_review, name='add_review'),
] 