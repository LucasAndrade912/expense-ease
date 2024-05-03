from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

Transaction_Types = models.TextChoices("incoming", "expense")


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email


class Transaction(Base):
    transaction_type = models.CharField(
        max_length=100, choices=Transaction_Types.choices
    )
    value = models.DecimalField(decimal_places=2, max_digits=20)
    category = models.CharField(max_length=120, blank=True, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    payment_method = models.CharField(max_length=80, blank=True, default="")
