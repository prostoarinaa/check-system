from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_slug


# class Student(models.Model):
#     name = models.CharField(
#         verbose_name="ФИО ученика",
#         max_length=100,
#         unique=True,
#         blank=False
#     )


class User(AbstractUser):
    username = models.CharField(
        verbose_name="Никнейм",
        max_length=150,
        unique=True,
        validators=[validate_slug]
    )
    fullname = models.CharField(
        verbose_name="ФИО",
        blank=False,
        null=False,
        max_length=150,
    )
    email = models.EmailField(
        verbose_name='E-mail',
        blank=True,
        unique=False,
        null=True
    )
    email_checked = models.DateTimeField(
        blank=True,
        null=True
    )

