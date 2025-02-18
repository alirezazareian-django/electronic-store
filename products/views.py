from rest_framework import viewsets
from .models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import CustomerFeedback
from .serializers import CustomerFeedbackSerializer
#اینپورت های مربوط به wishlist
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Wishlist
from .serializers import WishlistSerializer

from django.core.cache import cache
from products.tasks import update_product_cache

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        cache_key = "category_list"
        categories = cache.get(cache_key)

        if not categories:
            categories = Category.objects.all()
            cache.set(cache_key, categories, timeout=60 * 5)  # ۵ دقیقه

        return categories

    def perform_create(self, serializer):
        instance = serializer.save()
        cache.delete("category_list")  # حذف کش بعد از ایجاد

    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete("category_list")  # حذف کش بعد از بروزرسانی

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("category_list")  # حذف کش بعد از حذف

    
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CustomerFeedbackViewSet(viewsets.ModelViewSet):
    queryset = CustomerFeedback.objects.all().order_by('-created_at')
    serializer_class = CustomerFeedbackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # کاربر را به صورت خودکار به مدل اضافه می‌کند
        serializer.save(user=self.request.user)

class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['DELETE'], url_path='remove/(?P<product_id>\d+)')
    def remove_from_wishlist(self, request, product_id=None):
        """ حذف محصول از لیست علاقه‌مندی‌ها """
        wishlist_item = Wishlist.objects.filter(user=request.user, product_id=product_id).first()
        if wishlist_item:
            wishlist_item.delete()
            return Response({"message": "محصول از لیست علاقه‌مندی‌ها حذف شد."}, status=204)
        return Response({"error": "محصول یافت نشد."}, status=404)
