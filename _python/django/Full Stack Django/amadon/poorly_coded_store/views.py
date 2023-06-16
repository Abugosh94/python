from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    if "total_price" not in request.session:
        y=0
        request.session["total_orders"]= 0
        for x in Order.objects.all():
            y += x.total_price
            request.session["total_orders"] += x.quantity_ordered
        request.session["total_price"] = str(y)
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = request.session["quantity"]
    price_from_form = float(request.session["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    last_order = Order.objects.last()
    y= float(request.session["total_price"])
    y += total_charge
    request.session["total_orders"] += last_order.quantity_ordered
    request.session["total_price"] = str(round(y,2))
    return redirect("/checkout_page")

def order(request, id):
    prod = Product.objects.get(id=id)
    request.session["price"] = str(prod.price)
    request.session["quantity"]= int(request.POST["quantity"])
    return redirect("/checkout")

def checkout_page(request):
    context = {
        "latest_order": Order.objects.last(),
    }
    return render(request, "store/checkout.html", context)

def clear(request):
    request.session.clear()
    return redirect("/")