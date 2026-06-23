from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buy/<int:id>/', views.buy_product, name='buy_product'),
]