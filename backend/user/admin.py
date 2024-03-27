from django.contrib import admin

# Register your models here.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)
from django.contrib import messages
from django.utils.translation import ngettext

from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()

# @admin.register(User)
# class UserAdmin(AuthUserAdmin):
#     fieldsets = (
#         (None,
#             {
#                 "fields": (
#                     (("username", "email", ), "password", "is_active", )
#                 )
#             },
#         ),
#         ("Date Information",
#             {
#                 "fields": (("date_joined", "last_login"),),
#                 "classes": ("collapse"),
#             },
#         ),
#         ('Permissions', 
#             {
#                 'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
#                 'classes': ('collapse', 'collapse-closed'),
#             }
#         ),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("email", "password1", "password2"),
#             },
#         ),
#     )
#     form = UserChangeForm
#     add_form = UserCreationForm
#     change_password_form = AdminPasswordChangeForm
#     list_display = ("email", "username", "last_login", "is_active", "date_joined")
#     list_display_links = ("email",)
#     ordering = ("id",)
#     list_filter = ("is_active", "is_staff", "is_superuser", "date_joined")
#     search_fields = ("username", "email")
#     date_hierarchy = "date_joined"
#     filter_horizontal = (
#         "groups",
#         "user_permissions",
#     )
