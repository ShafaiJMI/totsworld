from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class CustomAccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,password,**other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,username,first_name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
                raise ValueError(_('Please assign is_staff=True for superuser'))
        if other_fields.get('is_superuser') is not True:
                raise ValueError(_('Please assign is_superuser=True for superuser'))
        return self.create_user(email,username,first_name,password,**other_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True)
    username= models.CharField(('User Name'),max_length=150)
    first_name = models.CharField(('First Name'),max_length=150)
    last_name = models.CharField(('last Name'),max_length=150)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects=CustomAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name']
    
    def __str__(self):
        return self.email