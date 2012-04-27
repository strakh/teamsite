from django.db import models
from django.contrib.auth.models import User

class Images(models.Model):    
    title = models.CharField(max_length=60)
    url = models.CharField(max_length=600)
    #text = models.CharField(max_length=600)
    #autor = models.OneToOneField(Employee, blank = True, null = True)

class Employee(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField()
    specialization = models.CharField(max_length=60)
    education = models.CharField(max_length=60)
    skils = models.CharField(max_length=60)
    info = models.CharField(max_length=600)
    user_no = models.OneToOneField(User, blank = True, null = True)
    img = models.OneToOneField(Images, blank = True, null = True)
    
    def __unicode__(self):
         return u'Employee %s' % self.name
        
class Projects(models.Model):
    name = models.CharField(max_length=30)
    url_address = models.URLField()
    info = models.CharField(max_length=50)
    date_start = models.DateField()
    klient = models.CharField(max_length=30)
    autors = models.ManyToManyField(Employee)

class Article(models.Model):    
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now = True)
    text = models.CharField(max_length=600)
    autor = models.OneToOneField(Employee, blank = True, null = True)
    img = models.ManyToManyField(Images)

"""    
class Price(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
"""    
    
# Create your models here.
