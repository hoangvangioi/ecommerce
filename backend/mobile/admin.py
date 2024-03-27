from django.contrib import admin
from .models import Mobile

# Register your models here.


class MobileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def __init__(self, model, admin_site):
        self.form.admin_site = admin_site
        super(MobileAdmin, self).__init__(model, admin_site)


admin.site.register(Mobile, MobileAdmin)
