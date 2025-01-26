from rest_framework import viewsets
from .models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import CustomerFeedback
from .serializers import CustomerFeedbackSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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
