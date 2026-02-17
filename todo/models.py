from django.db import models
from datetime import timedelta, datetime
import calendar

# Create your models here.

now = datetime.now().time()

class Todo(models.Model):
    body = models.CharField(max_length=255)
    duration = models.FloatField(default=1.0)
    
    status_type_choices =(
        ("new", "yangi"),
        ("processing","davom etmoqda.."),
        ("done", "bajarilgan")
        
    )
    duration_type_choices =(
        
        ("minute", "daqiqa"),
        ("hour","soat"),
        ("day", "kun"),
        ("week","hafta"),
        ("month","oy"),
        ("year", "yil")
    )
    
    duration_type = models.CharField(max_length=15, choices=duration_type_choices)
    status = models.CharField(max_length=11, choices=status_type_choices,default="new")
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.body[:55]
    
    def duration_range(self):
        if self.duration_type == "minute":
            return self.created_at + timedelta (minutes=self.duration)
        
        if self.duration_type == "hour":
            return self.created_at + timedelta (hours=self.duration)
        
        if self.duration_type == "day":
            return self.created_at + timedelta (days=self.duration)
        
        if self.duration_type == "week":
            return self.created_at + timedelta (weeks=self.duration)
        
        if self.duration_type == "month":
            year = datetime.now().year
            month = datetime.now().month
            
            fisrt_day, days_count = calendar.monthrange(year,month)
            return self.created_at + timedelta(days=days_count)
        
        if self.duration_type == "year":
            year = datetime.now().year
            if year % 4 == 0:
                days_in_thisyear = 365
            else:
                days_in_thisyear = 366
                
            return self.created_at + timedelta (days=days_in_thisyear)