from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Employee(models.Model):
    empid = models.CharField(primary_key=True,max_length=5)
    firstname = models.CharField(max_length=100,blank=False)
    lastname = models.CharField(max_length=100,blank=False)
    photo = models.ImageField(upload_to='employeeprofile/images/',default='myphoto')
    email = models.EmailField(max_length = 254,default='email@company.com')
    password = models.CharField(max_length=10,blank=False,default='password')
    phone = models.CharField(max_length=10,blank=False,default='1234567890')
    address = models.CharField(max_length=20,default='home')


    def __str__(self):
        return self.firstname

