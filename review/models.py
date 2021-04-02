from django.db import models
from django.utils import timezone

class Review(models.Model):

    """model to save reviews"""

    name = models.CharField(max_length=150)
    number = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
 
    time = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.name
