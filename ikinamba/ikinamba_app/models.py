from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin,Group,Permission
from django.core.validators import RegexValidator

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number must be set')
        extra_fields.setdefault('is_active', True)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone_number, password, **extra_fields)
class Myuser(AbstractUser):
    ROLE_CHOICES = [
        ('Employee', 'Employee'),
        ('Superadmin', 'Superadmin'),
        ('User', 'User'),
    ]
    GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ]
    
    username=None
    phone_number=models.CharField(max_length=10,validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Phone number must be 10 digits long.",
                code='invalid_phone_number'
            )
            ],
        unique=True)
    email=models.EmailField(unique=True,blank=True)
    role=models.CharField(choices=ROLE_CHOICES,max_length=50)
    gender= models.CharField(choices=GENDER_CHOICES,max_length=20)
    need_password_change=models.BooleanField(default=True)
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=['email']
    
    object=CustomUserManager()
    def __str__(self):
        return self.phone_number
    


class ikinamba(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    chief_name = models.CharField(max_length=255)
    contact_address =models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    body_type = models.CharField(max_length=50)
    wash_price = models.DecimalField(max_digits=8,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} {self.model}({self.manufacturer})'

class Service(models.Model):
    name = models.CharField(max_length=100)        # Service name, e.g., "Basic Wash"
    description = models.TextField()               # Service description
    duration = models.PositiveIntegerField()       # Duration in minutes
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price of the service
    created_at = models.DateTimeField(auto_now_add=True)         # Auto timestamp when the service is added

    def __str__(self):
        return self.name

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
# Create your models here.
