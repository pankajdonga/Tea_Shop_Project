from django.contrib import admin
from manager.models import *
# Register your models here.

class ProductModelData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','product_name','quantity']

class CategoryData(admin.ModelAdmin):
    list_display=['add_category']

admin.site.register(ProductModel,ProductModelData)
admin.site.register(ProductCategoryModel,CategoryData)
admin.site.register(staff)
admin.site.register(StaffAttendance)

