from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [

    # ===========================
    # HOME
    # ===========================

    path(
        "",
        views.home,
        name="home"
    ),

    # ===========================
    # PRODUCTS
    # ===========================

    path(
        "buy/<int:id>/",
        views.buy_product,
        name="buy_product"
    ),

    # ===========================
    # SHOPPING CART
    # ===========================

    path(
        "cart/",
        views.cart,
        name="cart"
    ),

    path(
        "cart/add/<int:id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),
path(
    "cart/remove/<int:id>/",
    views.remove_from_cart,
    name="remove_from_cart"
),

path(
    "cart/increase/<int:id>/",
    views.increase_quantity,
    name="increase_quantity"
),

path(
    "cart/decrease/<int:id>/",
    views.decrease_quantity,
    name="decrease_quantity"
),
    # ===========================
    # AUTHENTICATION
    # ===========================

    path(
        "signup/",
        views.signup,
        name="signup"
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),

    # ===========================
    # USER
    # ===========================

    path(
        "profile/",
        views.profile,
        name="profile"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    # ===========================
    # ADMIN
    # ===========================

    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

]