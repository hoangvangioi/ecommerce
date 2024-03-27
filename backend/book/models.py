from django.db import models
from django.db.models.signals import pre_save
from common.utils import pre_save_slug_receiver
from common.models import BaseModel

# Create your models here.


class Book(BaseModel):
    author = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="book", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book:", kwargs={"slug": self.slug})

    class Meta:
        db_table = "book"
        verbose_name = "Book"
        verbose_name_plural = "Books"


pre_save.connect(pre_save_slug_receiver, sender=Book)
