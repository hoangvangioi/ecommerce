from django.contrib import admin
from .models import Cart

# Register your models here.


class CartAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.form.admin_site = admin_site
        super(CartAdmin, self).__init__(model, admin_site)


admin.site.register(Cart, CartAdmin)
