from django.db import models

# Create your models here.

class ProductCategoryModel(models.Model):
    add_category=models.CharField(max_length=100)

    def __str__(self):
        return self.add_category


class ProductModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    product_name=models.CharField(max_length=100)
    select_category=models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField()
    description=models.TextField()
    product_img=models.ImageField(upload_to='media/')

class staff(models.Model):
    employee_name=models.CharField(max_length=100)
    employee_mobile=models.BigIntegerField()
    employee_email=models.EmailField()

    def __str__(self):
        return self.employee_name

class StaffAttendance(models.Model):
    staff=models.ForeignKey(staff,on_delete=models.CASCADE)
    punch_in=models.TimeField(blank=True,null=True)
    punch_out=models.TimeField(blank=True,null=True)
    date=models.DateField()
    status=models.CharField(max_length=20)
    
    def __str__(self):
        return self.staff.employee_name





