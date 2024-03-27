from django.db import models
from common.models import BaseModel
from django.db.models.signals import pre_save
from common.utils import pre_save_slug_receiver

# Create your models here.


class Mobile(BaseModel):
    brand = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="mobile", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "mobile"
        verbose_name = "Mobile"
        verbose_name_plural = "Mobiles"


pre_save.connect(pre_save_slug_receiver, sender=Mobile)
