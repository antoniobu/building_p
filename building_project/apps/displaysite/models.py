from django.db import models
from django.contrib.auth.models import User

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Модель товара
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    brand = models.CharField(max_length=255, default='Unknown Brand')  # Поле для бренда с дефолтным значением
    model = models.CharField(max_length=255, default='Unknown Model')   # Поле для модели
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    rating_1_star = models.PositiveIntegerField(default=0)
    rating_2_star = models.PositiveIntegerField(default=0)
    rating_3_star = models.PositiveIntegerField(default=0)
    rating_4_star = models.PositiveIntegerField(default=0)
    rating_5_star = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        total_reviews = self.rating_1_star + self.rating_2_star + self.rating_3_star + self.rating_4_star + self.rating_5_star
        if total_reviews == 0:
            return 0
        total_score = (self.rating_1_star * 1 + self.rating_2_star * 2 + self.rating_3_star * 3 + self.rating_4_star * 4 + self.rating_5_star * 5)
        return total_score / total_reviews

# Модель изображения для товара
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

# Модель заказа
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

# Модель элемента заказа
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

# Расширение модели пользователя
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Дополнительные поля профиля пользователя, если необходимы

# Сигналы для автоматического создания профиля пользователя
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
