from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from products.models import Product
from .models import Order


class CreateOrderView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(
            Product,
            slug=kwargs["slug"],
            status=Product.Status.PUBLISHED,
        )

        Order.objects.get_or_create(
            buyer=request.user,
            product=product,
            defaults={"status": Order.Status.PENDING},
        )

        return redirect("products:product_detail", slug=product.slug)


class MyOrdersView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        orders = request.user.orders.select_related("product").order_by("-created_at")
        return render(request, "orders/my_orders.html", {"orders": orders})