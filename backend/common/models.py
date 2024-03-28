from djongo import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from category.models import Category
# from django.contrib.auth.models import User
# from category.models import CustomUser

# Create your models here.


class BaseModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, unique_for_date='created_at')
    # auser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    quantity = models.IntegerField(default=10)
    description = models.TextField(max_length=500, default="Empty description.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_available(self):
        return self.quantity > 0

    class Meta:
        abstract = True
