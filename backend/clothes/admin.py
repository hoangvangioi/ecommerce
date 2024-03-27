from django.contrib import admin
from .models import Clothes

# Register your models here.


class ClothesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def __init__(self, model, admin_site):
        self.form.admin_site = admin_site
        super(ClothesAdmin, self).__init__(model, admin_site)


admin.site.register(Clothes, ClothesAdmin)
