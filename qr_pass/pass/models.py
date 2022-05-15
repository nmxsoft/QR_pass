from django.db import models


class Customer(models.Model):
    username = models.CharField(
        max_length=100,
        verbose_name='Кто заходит',
        unique=True

    )
    real_name = models.CharField(
        max_length=200,
        verbose_name='Реальный Пользователь'
    )
    access = models.BooleanField(default=False)

    def __str__(self):
        return self.username
