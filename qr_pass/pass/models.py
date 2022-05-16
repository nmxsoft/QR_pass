import datetime as dt
from django.db import models


def create_key():
    return (str(dt.datetime.now())
            .replace(' ', '')
            .replace('-', '')
            .replace(':', '')
            .replace('.', '')
            )


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
        default=create_key()
    )

    def __str__(self):
        return self.username
