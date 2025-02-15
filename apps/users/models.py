from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=150, verbose_name=_("Username"), unique=True)
    first_name = models.CharField(
        max_length=150,
        verbose_name=_("First Name"),
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name=_("Last Name"),
    )
    email = models.EmailField(
        verbose_name=_("Email Address"),
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Staff Status"),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
    )
    date_joined = models.DateTimeField(
        verbose_name=_("Date Joined"),
        default=timezone.now,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name.title(), self.last_name.title()}"

    def get_sort_name(self):
        return self.username
