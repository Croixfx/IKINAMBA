from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

@admin.register(Myuser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'gender', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
        ('Other', {'fields': ('need_password_change',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'password1', 'password2', 'role', 'gender',  'is_staff', 'is_active'),
        }),
    )
    list_display = ('phone_number', 'email', 'role', 'gender', 'is_staff', 'is_active', 'need_password_change')
    search_fields = ('phone_number', 'email', 'first_name', 'last_name')
    ordering = ('date_joined',)
    list_filter = ('role', 'gender', 'is_staff', 'is_active')


admin.site.register(ikinamba)
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Subscription)




# Register your models here.
