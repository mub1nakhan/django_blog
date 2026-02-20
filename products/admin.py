from django.contrib import admin

# Register your models here.
from .models import Category,Product


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ["id",""]
    


admin.site.register(Category)
admin.site.register(Product)