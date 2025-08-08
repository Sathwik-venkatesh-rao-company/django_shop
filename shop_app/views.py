from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
import json

def home(request):
    """Home page with featured products and categories"""
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:8]
    categories = Category.objects.all()[:6]
    latest_products = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'latest_products': latest_products,
    }
    return render(request, 'shop_app/home.html', context)

def product_list(request):
    """Product listing page with filtering and search"""
    products = Product.objects.filter(is_active=True)
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )
    
    # Category filter
    category_slug = request.GET.get('category', '')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    # Gender filter
    gender = request.GET.get('gender', '')
    if gender:
        products = products.filter(gender=gender)
    
    # Price filter
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    
    # Sort products
    sort_by = request.GET.get('sort', 'newest')
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    elif sort_by == 'name':
        products = products.order_by('name')
    else:
        products = products.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'products': page_obj,
        'categories': categories,
        'search_query': search_query,
        'current_category': category_slug,
        'current_gender': gender,
        'min_price': min_price,
        'max_price': max_price,
        'sort_by': sort_by,
    }
    return render(request, 'shop_app/product_list.html', context)

def product_detail(request, slug):
    """Product detail page"""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]
    
    # Get reviews
    reviews = product.reviews.all()
    
    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
    }
    return render(request, 'shop_app/product_detail.html', context)

def category_detail(request, slug):
    """Category detail page"""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_active=True)
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'products': page_obj,
    }
    return render(request, 'shop_app/category_detail.html', context)

def get_or_create_cart(request):
    """Helper function to get or create cart"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key, user=None)
    return cart

def add_to_cart(request):
    """Add product to cart via AJAX"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            quantity = int(data.get('quantity', 1))
            size = data.get('size', '')
            
            product = get_object_or_404(Product, id=product_id, is_active=True)
            cart = get_or_create_cart(request)
            
            # Check if item already exists in cart
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product,
                size=size,
                defaults={'quantity': quantity}
            )
            
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            
            return JsonResponse({
                'success': True,
                'message': f'{product.name} added to cart!',
                'cart_count': cart.items.count()
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

def update_cart_item(request):
    """Update cart item quantity via AJAX"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')
            quantity = int(data.get('quantity', 1))
            
            cart_item = get_object_or_404(CartItem, id=item_id)
            
            if quantity <= 0:
                cart_item.delete()
                message = 'Item removed from cart'
            else:
                cart_item.quantity = quantity
                cart_item.save()
                message = 'Cart updated successfully'
            
            return JsonResponse({
                'success': True,
                'message': message
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

def remove_from_cart(request):
    """Remove item from cart via AJAX"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')
            
            cart_item = get_object_or_404(CartItem, id=item_id)
            cart_item.delete()
            
            return JsonResponse({
                'success': True,
                'message': 'Item removed from cart'
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

def cart_view(request):
    """Shopping cart page"""
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()
    
    # Calculate totals
    subtotal = sum(item.total_price for item in cart_items)
    shipping = 0 if subtotal > 1000 else 100  # Free shipping over ₹1000
    total = subtotal + shipping
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
    }
    return render(request, 'shop_app/cart.html', context)

@login_required
def checkout(request):
    """Checkout page"""
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()
    
    if not cart_items.exists():
        messages.warning(request, 'Your cart is empty!')
        return redirect('shop:cart')
    
    # Calculate totals
    subtotal = sum(item.total_price for item in cart_items)
    shipping = 0 if subtotal > 1000 else 100
    total = subtotal + shipping
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create order
            order = Order.objects.create(
                user=request.user,
                total_amount=total,
                shipping_address=form.cleaned_data['shipping_address'],
                shipping_city=form.cleaned_data['shipping_city'],
                shipping_state=form.cleaned_data['shipping_state'],
                shipping_zip=form.cleaned_data['shipping_zip'],
                shipping_country=form.cleaned_data['shipping_country'],
                phone=form.cleaned_data['phone'],
                payment_method=form.cleaned_data['payment_method'],
                notes=form.cleaned_data['notes'],
            )
            
            # Create order items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.current_price,
                    size=cart_item.size,
                )
            
            # Clear cart
            cart.delete()
            
            messages.success(request, f'Order placed successfully! Order ID: {order.order_id}')
            return redirect('shop:order_confirmation', order_id=order.order_id)
    else:
        # Pre-fill form with user profile data
        try:
            profile = request.user.userprofile
            initial_data = {
                'shipping_address': profile.address,
                'shipping_city': profile.city,
                'shipping_state': profile.state,
                'shipping_zip': profile.zip_code,
                'shipping_country': profile.country,
                'phone': profile.phone,
            }
            form = CheckoutForm(initial=initial_data)
        except UserProfile.DoesNotExist:
            form = CheckoutForm()
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
        'form': form,
    }
    return render(request, 'shop_app/checkout.html', context)

@login_required
def order_confirmation(request, order_id):
    """Order confirmation page"""
    order = get_object_or_404(Order, order_id=order_id, user=request.user)
    return render(request, 'shop_app/order_confirmation.html', {'order': order})

@login_required
def order_history(request):
    """User's order history"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop_app/order_history.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    """Order detail page"""
    order = get_object_or_404(Order, order_id=order_id, user=request.user)
    return render(request, 'shop_app/order_detail.html', {'order': order})

def register(request):
    """User registration"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('shop:home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'shop_app/register.html', {'form': form})

@login_required
def profile(request):
    """User profile page"""
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('shop:profile')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'shop_app/profile.html', {'form': form})

@login_required
def add_review(request, product_id):
    """Add product review"""
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('shop:product_detail', slug=product.slug)
    else:
        form = ReviewForm()
    
    return render(request, 'shop_app/add_review.html', {
        'form': form,
        'product': product
    })
