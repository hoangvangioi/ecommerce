from django.db import models
from django.contrib.auth import get_user_model
from book.models import Book
from clothes.models import Clothes
from mobile.models import Mobile

# Create your models here.


User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    session = models.CharField(blank=True, max_length=100)
    quantity = models.IntegerField(default=1)

    book = models.ManyToManyField(Book, blank=True)
    clothes = models.ManyToManyField(Clothes, blank=True)
    mobile = models.ManyToManyField(Mobile, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.user, self.session)

    @property
    def count(self):
        return self.cartitem_set.count()

    @property
    def cart_price(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.item_total
        return total

    @property
    def total_count(self):
        cart_count = 0
        for item in self.cartitem_set.all():
            cart_count += item.quantity
        return cart_count

    class Meta:
        db_table = "cart"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
