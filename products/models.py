from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/')
    specifications = models.JSONField()  # برای مشخصات فنی محصول

    def __str__(self):
        return self.name

class CustomerFeedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='feedbacks')
    comment = models.TextField()
    rating = models.PositiveIntegerField()  # امتیاز از 1 تا 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.rating}/5"




