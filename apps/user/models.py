from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import uuid

nb = dict(null=True, blank=True)

class UserCustom(UserManager):
    use_in_migrations = True


    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)
    

class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(verbose_name='Имя', max_length=20)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    username = models.EmailField(verbose_name='Электронная почта', max_length=254, **nb, unique=True)
    # is_staff = models.BooleanField("staff status", default=False,)
    is_active = models.BooleanField("active", default=True,)
    password = models.CharField(verbose_name='Пароль', max_length=254, null=False, blank=False)
    delivery_address = models.CharField(verbose_name='Адрес доставки', max_length=254, **nb)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=254, **nb)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
