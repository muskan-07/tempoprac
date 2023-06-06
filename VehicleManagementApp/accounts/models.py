from django.db import models

# Create your models here.

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
alphanumeric = RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, email, Name,Contact ,password=None,password2=None):
        """
        Creates and saves a User with the given email, name , contact,
        password 
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            Name=Name,
            Contact=Contact,
            
        )
  
 
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, Name,Contact, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            Name=Name,
            Contact=Contact
        )
        user.Is_admin = False
        user.Is_superuser=True
        user.save(using=self._db)
        return user

    def create_adminuser(self, email, Name,Contact, password=None,password2=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            Name=Name,
            Contact=Contact
        )
        user.Is_admin = True
        user.Is_superuser=False
        user.save(using=self._db)
        return user


        

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    Name=models.CharField(max_length=200)
    Contact=models.BigIntegerField()
    Created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)
    Is_active = models.BooleanField(default=True)
    Is_admin = models.BooleanField(default=False)
    Is_superuser=models.BooleanField(default=False)
    Created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Name','Contact']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.Is_superuser

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.Is_superuser

VEHICLETYPE=(
        ('TwoWheeler','TwoWheeler'),
        ('ThreeWheeler','ThreeWheeler'),
        ('FourWheeler','FourWheeler'),
    )
class VehicleDetails(models.Model):
    VehicleNumber=models.CharField(max_length=12,validators=[alphanumeric])
    VehicleType=models.CharField(max_length=20,choices=VEHICLETYPE)
    VehicleModel=models.CharField(max_length=60)
    VehicleDescription=models.CharField(max_length=300)

    def __str__(self):
        return self.VehicleNumber