from django.db import models

# Simple Database model
class TodoItem(models.Model): 
    title = models.CharField(max_length=200) 
    completed = models.BooleanField(default=False)
