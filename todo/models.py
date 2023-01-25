
from django.db import models

status_choices = [
    ('C', 'Completed'),
    ('P', 'Pending'),
]

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=status_choices)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title