from django.db import models


class Customer(models.Model):
    username = models.TextField(
        max_length=100,
        verbose_name='Кто заходит'
    )
    real_name = models.TextField(
        max_length=200,
        verbose_name='Реальный Пользователь'
    )
    access = models.BooleanField(default=False)

    def __str__(self):
        return self.username
