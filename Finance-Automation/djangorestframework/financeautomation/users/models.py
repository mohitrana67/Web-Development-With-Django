from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import datetime

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, age, password=None):
        if not email:
            raise ValueError("User must have an email to register with")
        if not username:
            raise ValueError("User must have a unique username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name,
            age=age
        )

        user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, age, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            age=age
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# This will define the dependencies of a user/
class User(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date jpined', auto_now=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=datetime.date.today)
    profile_pic = models.ImageField(upload_to='image', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','age']

    object = MyAccountManager()

    def __str__(self):
        return self.username + "," + self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perm(self, app_label):
        return True