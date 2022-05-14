from django.contrib import admin

from .models import Customer

@admin.register(Customer)
class PassRegister(admin.ModelAdmin):
    list_display = (
        'username',
        'real_name',
        'access',
    )