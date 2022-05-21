from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Customer(models.Model):
    username = models.CharField(
        max_length=100,
        verbose_name='Ник посетителя',
        unique=True
    )
    real_name = models.CharField(
        max_length=200,
        verbose_name='Реальное имя посетителя',
        blank=True
    )
    access = models.BooleanField(
        default=False,
        verbose_name='Доступ'
    )
    key = models.CharField(
        max_length=20,
        verbose_name='секретный ключ',
        default='11111111111111111111'
    )
    master = models.ForeignKey(
        User,
        verbose_name="Создатель",
        on_delete=models.CASCADE,
        related_name='customers'
    )

    def __str__(self):
        return self.username


class Logs(models.Model):
    user = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name='Ник посетителя',
        related_name='logos'

    )
    visit = models.DateTimeField(
        verbose_name='Время входа',
        auto_now_add=True
    )
    success = models.BooleanField(
        verbose_name='Попытка входа',
        default=False
    )

    class Meta:
        ordering = ('-visit',)
