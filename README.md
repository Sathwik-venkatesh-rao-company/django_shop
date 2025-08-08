# 🛍️ Fashion Store - E-commerce Web Application

A full-stack e-commerce web application built with Django, HTML, CSS, and JavaScript for a clothing store. This application provides a complete online shopping experience with modern UI/UX design.

## ✨ Features

### 🏠 **Home Page**
- Hero section with call-to-action buttons
- Featured products showcase
- Category browsing
- Latest arrivals section
- Responsive design for all devices

### 🛒 **Product Management**
- Product catalog with filtering and search
- Product detail pages with image galleries
- Size selection and stock management
- Product reviews and ratings
- Related products suggestions

### 🔍 **Search & Filtering**
- Product search functionality
- Category-based filtering
- Gender-based filtering
- Price range filtering
- Sort by price, name, and date
- Grid and list view options

### 🛍️ **Shopping Cart**
- Add/remove items from cart
- Quantity adjustment
- Real-time cart updates
- Cart persistence (session-based)
- Cart summary with totals

### 👤 **User Management**
- User registration and authentication
- User profile management
- Order history tracking
- Address management

### 💳 **Checkout Process**
- Secure checkout form
- Shipping information collection
- Payment method selection
- Order confirmation
- Order tracking

### 📱 **Admin Panel**
- Product management
- Category management
- Order management
- User management
- Review management

## 🛠️ Technology Stack

### Backend
- **Django 5.2** - Web framework
- **SQLite** - Database (can be easily changed to PostgreSQL/MySQL)
- **Pillow** - Image processing

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling with custom design
- **JavaScript** - Interactive functionality
- **Bootstrap 5.3** - Responsive framework
- **Font Awesome** - Icons

### Key Features
- **Responsive Design** - Works on all devices
- **AJAX Integration** - Real-time cart updates
- **Session Management** - Cart persistence
- **Image Upload** - Product image management
- **Search & Filter** - Advanced product discovery

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Shop_project
```

### Step 2: Create Virtual Environment
```bash
# Using conda (recommended)
conda create -n ShopEnv python=3.11
conda activate ShopEnv

# Or using venv
python -m venv ShopEnv
source ShopEnv/bin/activate  # On Windows: ShopEnv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser
```bash
python manage.py createsuperuser
```

### Step 6: Populate Sample Data
```bash
python manage.py populate_sample_data
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📁 Project Structure

```
Shop_project/
├── manage.py
├── requirements.txt
├── README.md
├── Shop_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── shop_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── management/
│   │   └── commands/
│   │       └── populate_sample_data.py
│   └── migrations/
├── template/
│   └── shop_app/
│       ├── base.html
│       ├── home.html
│       ├── product_list.html
│       ├── product_detail.html
│       ├── cart.html
│       ├── checkout.html
│       ├── register.html
│       ├── profile.html
│       └── order_confirmation.html
├── static/
├── media/
└── db.sqlite3
```

## 🗄️ Database Models

### Core Models
- **Category** - Product categories
- **Product** - Product information with pricing
- **ProductImage** - Product image management
- **UserProfile** - Extended user information
- **Cart/CartItem** - Shopping cart functionality
- **Order/OrderItem** - Order management
- **Review** - Product reviews and ratings

## 🎨 Design Features

### Color Scheme
- Primary: #2c3e50 (Dark Blue)
- Secondary: #e74c3c (Red)
- Accent: #3498db (Blue)
- Success: #27ae60 (Green)

### UI Components
- Modern card-based design
- Hover effects and animations
- Responsive grid layouts
- Interactive buttons and forms
- Professional typography

## 🔧 Configuration

### Settings
- Debug mode enabled for development
- Static and media files configured
- Database settings (SQLite by default)
- Installed apps configured

### URLs
- Main app URLs included
- Admin panel accessible at `/admin/`
- Authentication URLs included

## 📊 Sample Data

The application comes with sample data including:
- 5 product categories
- 8 sample products
- Featured and sale items
- Various sizes and pricing

## 🛡️ Security Features

- CSRF protection enabled
- User authentication required for checkout
- Form validation
- Secure password handling
- Session management

## 🚀 Deployment

### For Production
1. Set `DEBUG = False` in settings.py
2. Configure a production database (PostgreSQL/MySQL)
3. Set up static file serving
4. Configure environment variables
5. Use a production WSGI server (Gunicorn)

### Environment Variables
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=your-database-url
```

## 📱 Features Overview

### Customer Features
- ✅ Browse products by category
- ✅ Search and filter products
- ✅ Add items to cart
- ✅ Manage shopping cart
- ✅ User registration and login
- ✅ Complete checkout process
- ✅ Order tracking
- ✅ Product reviews
- ✅ User profile management

### Admin Features
- ✅ Product management
- ✅ Category management
- ✅ Order management
- ✅ User management
- ✅ Review moderation
- ✅ Sales analytics

## 🔄 Future Enhancements

### Planned Features
- [ ] Payment gateway integration (Stripe/PayPal)
- [ ] Email notifications
- [ ] Wishlist functionality
- [ ] Advanced search with filters
- [ ] Product recommendations
- [ ] Inventory management
- [ ] Discount codes
- [ ] Multi-language support
- [ ] Mobile app
- [ ] Analytics dashboard

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Created with ❤️ for the Fashion Store e-commerce platform.

## 📞 Support

For support and questions:
- Email: support@fashionstore.com
- Phone: +91 98765 43210

---

**Happy Shopping! 🛍️** 