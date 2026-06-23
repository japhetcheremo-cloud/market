from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def buy_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')

        message = f"""
Hello Cheremo Promised Shop

Product: {product.name}
Price: Ksh {product.price}

Customer Name: {name}
Phone: {phone}
Location: {location}
"""

        whatsapp_number = "254719678760"

        whatsapp_link = f"https://wa.me/{whatsapp_number}?text={message}"

        return render(request,'redirect.html',{
            'whatsapp_link': whatsapp_link
        })

    return render(request,'buy.html',{
        'product':product
    })