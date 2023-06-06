from django.contrib import admin
from accounts.models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin






class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'Contact', 'Is_admin','Is_superuser')
    list_filter = ('Is_admin','Is_superuser')
    fieldsets = (
        ('UserCredentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('Contact',)}),
        ('Permissions', {'fields': ('Is_admin','Is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'Contact', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.












# Register your models here.

admin.site.register(VehicleDetails)