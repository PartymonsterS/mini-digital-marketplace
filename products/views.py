from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import ProductCreateForm
from .models import Category, Product


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().order_by("name")
        return context


class CategoryProductListView(ListView):
    model = Product
    template_name = "products/category_product_list.html"
    context_object_name = "products"

    def dispatch(self, request, *args, **kwargs):
        self.category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return (
            Product.objects.filter(
                category=self.category,
                status=Product.Status.PUBLISHED,
            )
            .select_related("category", "seller")
            .order_by("-created_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Product.objects.filter(
            status=Product.Status.PUBLISHED
        ).select_related("category", "seller")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("products:my_products")

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class MyProductsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/my_products.html"
    context_object_name = "products"

    def get_queryset(self):
        return (
            Product.objects.filter(seller=self.request.user)
            .select_related("category")
            .order_by("-created_at")
        )