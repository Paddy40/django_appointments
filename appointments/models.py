from django.db import models
from django.forms import widgets

# from djwidgets import BootstrapDateTimePickerInput


# Create your models here.
class Doctable(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    descr = models.TextField()
    img = models.CharField(max_length=100)

class Patienttable(models.Model):
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Dont want to say',),
    )
    name = models.CharField(max_length=100)
    DoB= models.DateField(verbose_name='DOB(mm/dd/yyyy)')
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )
    phone= models.IntegerField()
    address = models.TextField()
    email=models.EmailField()
    history = models.TextField()




class Appointmenttable(models.Model):
    docname = models.CharField(max_length=100)
    doctid = models.IntegerField(default=0)
    patientname = models.CharField(max_length=100)
    patientid=models.IntegerField(default=0)
    date = models.DateField()
    time = models.CharField(max_length=5)



class Logintable(models.Model):
    uname = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100,default='abc')
    givenid= models.IntegerField(default=0)
    department = models.CharField(max_length=100)
    psswd=models.CharField(max_length=15)


class Querytable(models.Model):
    name = models.CharField(max_length=100)
    phone= models.IntegerField()
    email=models.EmailField()
    query = models.TextField()
