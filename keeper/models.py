from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from keeper.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', primary_key=True, db_column="EMAIL")
    is_staff = models.BooleanField(default=False, db_column="IS_STAFF")
    is_active = models.BooleanField(default=True, db_column="IS_ACTIVE")
    date_joined = models.DateTimeField(default=timezone.now, db_column="CREATE_DTTM")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return self.email


class UsersData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=50, null=True, blank=True, db_column="SERVICE_NAME")
    login = models.CharField(max_length=50, null=True, blank=True, db_column="LOGIN")
    password = models.CharField(max_length=256, null=False, blank=False, db_column="PASSWORD")
    update_date = models.DateTimeField(auto_now=True, db_column="UPDATE_DTTM")

    class Meta:
        db_table = "USER_DATA"
