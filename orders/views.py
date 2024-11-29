from django.shortcuts import render

# Create your views here.
# views.py (inside the 'orders' app)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order, OrderItem
from trees.models import Cart  # Assuming cart items are in the 'cart' app
from django.contrib.auth.decorators import login_required

@login_required
def place_order(request):
    # Fetch cart items for the logged-in user
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items:
        return HttpResponse("Your cart is empty.", status=400)

    # Calculate the total price
    total_price = sum(item.subtotal for item in cart_items)

    # Create an order for the user
    order = Order.objects.create(user=request.user, total_price=total_price)

    # Add items to the order
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            tree=item.tree,
            quantity=item.quantity,
            subtotal=item.subtotal
        )

    # Optionally, delete the cart items after placing the order
    cart_items.delete()

    return redirect('order_confirmation', order_id=order.id)

@login_required
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'order_confirmation.html', {'order': order})

