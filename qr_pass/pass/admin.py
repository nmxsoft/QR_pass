from django.contrib import admin

from .models import Customer, Logs


@admin.register(Customer)
class PassRegister(admin.ModelAdmin):
    list_display = (
        'username',
        'real_name',
        'access',
        'key',
        'master'
    )


@admin.register(Logs)
class LogsRegister(admin.ModelAdmin):
    list_display = (
        'user',
        'visit',
        'success'
    )
