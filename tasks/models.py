from django.db import models
from datetime import datetime, date

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        if isinstance(self.due_date, str):  
            self.due_date = datetime.strptime(self.due_date, "%Y-%m-%d").date()
        
   
        if self.due_date < date.today() and self.status in ['pending', 'in_progress']:
            self.status = 'overdue'

        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} - {self.status}"
