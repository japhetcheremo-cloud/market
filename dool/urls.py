from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('buy/<int:id>/', views.buy_product, name='buy_product'),

    path('signup/', views.signup, name='signup'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path(
    'admin-dashboard/',
    views.admin_dashboard,
    name='admin_dashboard'
),
]