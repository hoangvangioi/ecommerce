from djongo import models
from common.models import BaseModel
from django.db.models.signals import pre_save
from common.utils import pre_save_slug_receiver

# Create your models here.


class Clothes(BaseModel):
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=25)
    size = models.CharField(max_length=25)
    picture = models.ImageField(upload_to="clothes", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "clothes"
        verbose_name = "Clothes"
        verbose_name_plural = "Clothes"


pre_save.connect(pre_save_slug_receiver, sender=Clothes)
