from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin #Have to check what these 2 are 
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import IntegrityError

# Custom User Manager
class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password, user_type,**extra_fields):
        if not email:
            raise ValueError(_("You must provide an email address"))
        email = self.normalize_email(email)

        # this is how we can add the permissions
        """
        User types are cateogarized as follow
            1 = Superuser
            2 = Accountant
            3 = Viewer
        """
        
        extra_fields.setdefault('is_staff', True)   

        if user_type == 1:
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_staff', True) 
        elif user_type == 2:
            extra_fields.setdefault('is_staff', True)
        elif user_type == 3:
            extra_fields.setdefault('is_staff', False) 

        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user_type = 1
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Super user must be assigned to is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super user must be assigned to is_superuser=True")
        
        return self.create_user(email,username, first_name, last_name, password,user_type, **extra_fields)

# Custom Account Model For every user with email as the identifier
class Account(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_("email address"), max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Set the field you want to use as the login identifier
    USERNAME_FIELD = 'email'
    
    # Settings fields which are required. This will not allow user to register until they have first name and last name
    REQUIRED_FIELDS = ['username', 'first_name','last_name']

    objects = CustomAccountManager()

# Profile for every user with an account
class Profile(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='Date Of Borth')