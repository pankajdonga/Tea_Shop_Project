from django.db import models
from manager.models import *
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class CustomBaseManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Please Enter Valid Email Address...')
        
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_customer',True)
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_superuser',True)

        return self.create_user(email,password,**extra_fields)
    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    full_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    objects=CustomBaseManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []

    def __str__(self):
        return self.email
    

class CustomerModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    full_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    mobile=models.BigIntegerField()
    comapny_name=models.CharField(max_length=100,blank=True,null=True)
    comapny_id=models.BigIntegerField(blank=True,null=True)
    is_normal_user=models.BooleanField(default=False)
    is_comapny_user=models.BooleanField(default=False)

class cart_order(models.Model):
    order_date=models.DateField(auto_now_add=True)
    order_id=models.IntegerField()
    company_name=models.CharField(max_length=100,blank=True,null=True)
    company_id=models.BigIntegerField(blank=True,null=True)
    customer_name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    product_id=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    product_quantity=models.IntegerField()
    total=models.IntegerField()
    city=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    society=models.CharField(max_length=100)
    apartment_number=models.CharField(max_length=100)
    card_payment=models.BooleanField(default=False)
    upi_payment=models.BooleanField(default=False)
    cash_payment=models.BooleanField(default=False)
    order_status=models.BooleanField(default=False)
    delivery_status=models.BooleanField(default=False)
