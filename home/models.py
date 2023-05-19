from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class OngoingEvent(models.Model):
    name=models.CharField()
    Location=models.CharField()
    time= models.DateTimeField(null=True)
    image=models.ImageField(upload_to='images')

class PastEvent(models.Model):
    name=models.CharField()
    Location=models.CharField()
    time= models.DateTimeField(null=True)
    image=models.ImageField(upload_to='images')

class FutureEvent(models.Model):
    name=models.CharField()
    Location=models.CharField()
    time= models.DateTimeField(null=True)
    image=models.ImageField(upload_to='images')


class testimony(models.Model):
    Role_CHOICES = {
        'V': 'Volunteer',
        'T': 'Trainee',
        'P': 'Partner',
    }
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    statement = models.TextField()
    role = models.CharField(max_length=1, choices=Role_CHOICES.items())

class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    email = models.EmailField( unique=True)
    hear_about_us = models.CharField(max_length=255)
    message = models.TextField()
    cv = models.FileField(upload_to='volunteer_cvs/')

    def __str__(self):
        return self.name
class donor(models.Model):
    name= models.CharField(max_length=60)
    email= models.EmailField(max_length=100,blank=False,unique=True)
    contact= PhoneNumberField()
    
class contact(models.Model):
    name= models.CharField(max_length=60)
    email= models.EmailField(max_length=100, blank=False,unique=True)
    phone= PhoneNumberField(unique=True)
    message=models.TextField()

class team(models.Model):
    name= models.CharField(max_length=100)
    designation= models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True)
    def __str__(self):
        return self.name
    
class program(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    time=models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images', blank=True)
    details=models.TextField(max_length=300, default=0)
    facilitator=models.CharField(max_length=50, default=0)
    def __str__(self):
        return self.name
    
class Resource(models.Model):
    title= models.CharField(max_length=100)
    about=models.TextField(max_length=300 ,default=0)
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')
    
