from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser


# Configure our new user for Admin console
# Register it below
class UserCustomAdmin(UserAdmin):
    # we got this from the UserAdmin code. It's how we set what fields appear in admin iterface
    # when adding a new user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


# Register your models here.
admin.site.register(AppUser, UserCustomAdmin)
