from datetime import datetime
from django.db import models
# Create your models here.
class ContactData(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=10)
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=500)
    Date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.Name
    

class AddJob(models.Model):
    Title = models.CharField(max_length=200)
    ShortDescription = models.CharField(max_length=2000)
    LongDescription = models.CharField(max_length=2000)
    JobRole = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Experince = models.CharField(max_length=100)
    Date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.Title