from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def __init__(self, model, admin_site):
        self.form.admin_site = admin_site
        super(BookAdmin, self).__init__(model, admin_site)


admin.site.register(Book, BookAdmin)
