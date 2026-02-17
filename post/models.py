from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=323)
    
    
    def __str__(self):
        return self.title
    


class Meta:
    verbose_name = "Katagoriya"
    verbose_name_plural = "Katagoriyalar"
    ordering = ("title",)
    
    
class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.CharField(max_length=233,blank=True,null=True)
    body = models.TextField()
    status_choices = (
        
        ("draft", "Qoralama"),
        ("public","Ommaviy"),
        ("delated","O'chirilgan"),
        ("archieved","Arxivlangan")
    )
    
    
    status = models.CharField(max_length=15,choices=status_choices)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.body[:50] + "..." if len(self.body) > 50 else self.body