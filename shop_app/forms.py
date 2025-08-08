from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Review

class CheckoutForm(forms.Form):
    """Form for checkout process"""
    PAYMENT_CHOICES = [
        ('COD', 'Cash on Delivery'),
        ('ONLINE', 'Online Payment'),
    ]
    
    shipping_address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your complete shipping address'}),
        label='Shipping Address'
    )
    shipping_city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'City'})
    )
    shipping_state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'State'})
    )
    shipping_zip = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'ZIP Code'})
    )
    shipping_country = forms.CharField(
        max_length=100,
        initial='India',
        widget=forms.TextInput(attrs={'placeholder': 'Country'})
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
    )
    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        initial='COD',
        widget=forms.RadioSelect
    )
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Any special instructions or notes'}),
        label='Order Notes'
    )

class UserProfileForm(forms.ModelForm):
    """Form for user profile"""
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city', 'state', 'zip_code', 'country']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your address'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'ZIP Code'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
        }

class ReviewForm(forms.ModelForm):
    """Form for product reviews"""
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your experience with this product...'}),
        }
        labels = {
            'rating': 'Rating (1-5 stars)',
            'comment': 'Your Review'
        }

class CustomUserCreationForm(UserCreationForm):
    """Custom user registration form"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
    )
    first_name = forms.CharField(
        max_length=30, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'})
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'})
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            if field_name not in ['email', 'first_name', 'last_name']:  # Already styled above
                field.widget.attrs.update({'class': 'form-control'})
                if field_name == 'username':
                    field.widget.attrs.update({'placeholder': 'Choose a username'})
                elif field_name == 'password1':
                    field.widget.attrs.update({'placeholder': 'Enter your password'})
                elif field_name == 'password2':
                    field.widget.attrs.update({'placeholder': 'Confirm your password'})
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user 