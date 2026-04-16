from django.urls import path
from .views import HomeView, CategoryProductListView, ProductDetailView

app_name = "products"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("categories/<slug:slug>/", CategoryProductListView.as_view(), name="category_products"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
]