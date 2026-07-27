from urllib.parse import quote

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomSignupForm
from .models import Product, Cart


# ===========================
# HOME
# ===========================

def home(request):

    products = Product.objects.all().order_by("-created_at")

    cart_count = 0

    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()

    return render(
        request,
        "home.html",
        {
            "products": products,
            "cart_count": cart_count,
        },
    )


# ===========================
# ADD TO CART
# ===========================

@login_required
def add_to_cart(request, id):

    product = get_object_or_404(Product, id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("home")


# ===========================
# VIEW CART
# ===========================

@login_required
def cart(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.subtotal() for item in cart_items)

    return render(
        request,
        "cart.html",
        {
            "cart_items": cart_items,
            "total": total,
        },
    )
# ===========================
# REMOVE FROM CART
# ===========================

@login_required
def remove_from_cart(request, id):

    item = get_object_or_404(
        Cart,
        id=id,
        user=request.user
    )

    item.delete()

    return redirect("cart")


# ===========================
# INCREASE QUANTITY
# ===========================

@login_required
def increase_quantity(request, id):

    item = get_object_or_404(
        Cart,
        id=id,
        user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect("cart")


# ===========================
# DECREASE QUANTITY
# ===========================

@login_required
def decrease_quantity(request, id):

    item = get_object_or_404(
        Cart,
        id=id,
        user=request.user
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")

# ===========================
# BUY PRODUCT
# ===========================

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
            f"https://wa.me/{whatsapp_number}?text={quote(message)}"
        )

        return render(
            request,
            "redirect.html",
            {
                "whatsapp_link": whatsapp_link,
            },
        )

    return render(
        request,
        "buy.html",
        {
            "product": product,
        },
    )


# ===========================
# SIGNUP
# ===========================

def signup(request):

    if request.method == "POST":

        form = CustomSignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = CustomSignupForm()

    return render(
        request,
        "signup.html",
        {
            "form": form,
        },
    )


# ===========================
# DASHBOARD
# ===========================

@login_required
def dashboard(request):
    return render(request, "dashboard.html")


# ===========================
# PROFILE
# ===========================

@login_required
def profile(request):

    return render(
        request,
        "profile.html",
        {
            "user": request.user,
        },
    )


# ===========================
# ADMIN DASHBOARD
# ===========================

@login_required
def admin_dashboard(request):

    if not request.user.is_staff:
        return redirect("dashboard")

    context = {
        "total_products": Product.objects.count(),
        "total_users": User.objects.count(),
        "total_cart_items": Cart.objects.count(),
    }

    return render(
        request,
        "admin_dashboard.html",
        context,
    )