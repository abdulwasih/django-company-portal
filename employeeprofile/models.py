from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employeeprofile/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

