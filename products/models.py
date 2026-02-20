from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    name = models.CharField(max_length=222)
    price = models.FloatField()
    description = models.TextField()
    discount = models.IntegerField()
    stock = models.IntegerField()
    status_choices = (
        ("added","qo'shilgan"),
        ("on way","yo'lda"),
        ("cancel","bekor qilindi")
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    