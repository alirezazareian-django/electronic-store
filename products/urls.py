from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, BrandViewSet
from .views import CustomerFeedbackViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register('feedbacks', CustomerFeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
