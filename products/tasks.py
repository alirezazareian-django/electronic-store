

from celery import shared_task
from django.core.cache import cache
from .models import Product
from .serializers import ProductSerializer

@shared_task
def update_product_cache():
    """این تابع محصولات را از دیتابیس خوانده و کش را بروزرسانی می‌کند."""
    products = Product.objects.all()
    serialized_products = ProductSerializer(products, many=True).data  # سریالایز کردن داده‌ها
    cache.set('products_list', serialized_products, timeout=60 * 5)  # ذخیره در کش برای ۵ دقیقه
    return "Cache updated!"

