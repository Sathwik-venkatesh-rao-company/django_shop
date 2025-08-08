from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shop_app.models import Category, Product, ProductImage
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate database with sample categories and products'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create categories
        categories_data = [
            {
                'name': 'Men\'s Clothing',
                'slug': 'mens-clothing',
                'description': 'Stylish clothing for men including shirts, pants, and accessories.'
            },
            {
                'name': 'Women\'s Clothing',
                'slug': 'womens-clothing',
                'description': 'Fashionable clothing for women including dresses, tops, and accessories.'
            },
            {
                'name': 'Casual Wear',
                'slug': 'casual-wear',
                'description': 'Comfortable and stylish casual clothing for everyday wear.'
            },
            {
                'name': 'Formal Wear',
                'slug': 'formal-wear',
                'description': 'Professional and formal clothing for special occasions.'
            },
            {
                'name': 'Accessories',
                'slug': 'accessories',
                'description': 'Fashion accessories to complete your look.'
            }
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create products
        products_data = [
            {
                'name': 'Classic White T-Shirt',
                'slug': 'classic-white-tshirt',
                'category': categories['mens-clothing'],
                'description': 'A comfortable and versatile white t-shirt made from 100% cotton. Perfect for everyday wear.',
                'price': Decimal('599.00'),
                'sale_price': Decimal('449.00'),
                'stock': 50,
                'gender': 'M',
                'is_featured': True,
                'available_sizes': [['S', 'Small'], ['M', 'Medium'], ['L', 'Large'], ['XL', 'Extra Large']]
            },
            {
                'name': 'Denim Jeans',
                'slug': 'denim-jeans',
                'category': categories['mens-clothing'],
                'description': 'Classic blue denim jeans with a modern fit. Comfortable and durable for daily wear.',
                'price': Decimal('1299.00'),
                'stock': 30,
                'gender': 'M',
                'available_sizes': [['30', '30'], ['32', '32'], ['34', '34'], ['36', '36']]
            },
            {
                'name': 'Floral Summer Dress',
                'slug': 'floral-summer-dress',
                'category': categories['womens-clothing'],
                'description': 'Beautiful floral print dress perfect for summer days. Light and comfortable fabric.',
                'price': Decimal('899.00'),
                'sale_price': Decimal('699.00'),
                'stock': 25,
                'gender': 'F',
                'is_featured': True,
                'available_sizes': [['XS', 'Extra Small'], ['S', 'Small'], ['M', 'Medium'], ['L', 'Large']]
            },
            {
                'name': 'Casual Blouse',
                'slug': 'casual-blouse',
                'category': categories['womens-clothing'],
                'description': 'Elegant casual blouse suitable for both office and casual outings.',
                'price': Decimal('799.00'),
                'stock': 40,
                'gender': 'F',
                'available_sizes': [['S', 'Small'], ['M', 'Medium'], ['L', 'Large']]
            },
            {
                'name': 'Hooded Sweatshirt',
                'slug': 'hooded-sweatshirt',
                'category': categories['casual-wear'],
                'description': 'Comfortable hooded sweatshirt perfect for casual wear. Available in multiple colors.',
                'price': Decimal('999.00'),
                'stock': 35,
                'gender': 'U',
                'is_featured': True,
                'available_sizes': [['S', 'Small'], ['M', 'Medium'], ['L', 'Large'], ['XL', 'Extra Large']]
            },
            {
                'name': 'Formal Shirt',
                'slug': 'formal-shirt',
                'category': categories['formal-wear'],
                'description': 'Professional formal shirt suitable for office and formal occasions.',
                'price': Decimal('1499.00'),
                'stock': 20,
                'gender': 'M',
                'available_sizes': [['S', 'Small'], ['M', 'Medium'], ['L', 'Large'], ['XL', 'Extra Large']]
            },
            {
                'name': 'Leather Belt',
                'slug': 'leather-belt',
                'category': categories['accessories'],
                'description': 'High-quality leather belt with classic buckle design.',
                'price': Decimal('399.00'),
                'stock': 60,
                'gender': 'U',
                'available_sizes': [['S', 'Small'], ['M', 'Medium'], ['L', 'Large']]
            },
            {
                'name': 'Stylish Watch',
                'slug': 'stylish-watch',
                'category': categories['accessories'],
                'description': 'Elegant watch with leather strap. Perfect accessory for any outfit.',
                'price': Decimal('2499.00'),
                'sale_price': Decimal('1999.00'),
                'stock': 15,
                'gender': 'U',
                'is_featured': True,
                'available_sizes': [['ONE_SIZE', 'One Size']]
            }
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        ) 