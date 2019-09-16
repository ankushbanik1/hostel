from django.db import models

from django.db import models
 
class complain(models.Model):

    name = models.CharField('Name', max_length=120)
    Email = models.CharField(max_length=120)
    message = models.CharField(max_length = 600)

# Create your models here.
    def __str__(self):

        return self.name