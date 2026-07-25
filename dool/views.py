from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from .models import Product

from urllib.parse import quote

from .forms import CustomSignupForm


def home(request):
    products = Product.objects.all().order_by('-created_at')

    return render(
        request,
        'home.html',
        {
            'products': products
        }
    )


def buy_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        location = request.POST.get("location")

        message = f"""
🛒 NEW ORDER

Product: {product.name}
Price: KSh {product.price}

Customer Name: {name}
Phone: {phone}
Location: {location}
"""

        whatsapp_number = "254719678760"

        whatsapp_link = (
            f"https://wa.me/{whatsapp_number}"
            f"?text={quote(message)}"
        )

        return render(
            request,
            "redirect.html",
            {
                "whatsapp_link": whatsapp_link
            }
        )

    return render(
        request,
        "buy.html",
        {
            "product": product
        }
    )


def signup(request):

    if request.method == "POST":

        form = CustomSignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = CustomSignupForm()

    return render(
        request,
        'signup.html',
        {'form': form}
    )

@login_required
def profile(request):
    return render(
        request,
        'profile.html',
        {
            'user': request.user
        }
    )
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):

    if not request.user.is_staff:
        return redirect('dashboard')

    total_products = Product.objects.count()
    total_users = User.objects.count()

    context = {
        'total_products': total_products,
        'total_users': total_users,
    }

    return render(request, 'admin_dashboard.html', context)