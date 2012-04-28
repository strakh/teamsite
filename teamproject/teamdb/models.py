from django.db import models
from django.contrib.auth.models import User

#TODO: What about base model for created_by/created_at as we discussed?

#TODO: class name should be singlular
class Images(models.Model):    
    title = models.CharField(max_length=60)
    #TODO: ImageField is better here. 
    url = models.CharField(max_length=600)
    #text = models.CharField(max_length=600)
    #autor = models.OneToOneField(Employee, blank = True, null = True)

class Employee(models.Model):
    name = models.CharField(max_length=30)
    #TODO: Not sure we really need team member's address here, 
    # but we really need more contact info like skype or jabber
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    #TODO: What is date? birth date?
    date = models.DateField()
    #TODO: Not sure I understand what is it? maybe position in team?
    specialization = models.CharField(max_length=60)
    education = models.CharField(max_length=60)\
    #TODO: rename this to 'skills'
    skils = models.CharField(max_length=60)
    #TODO: i think TextField is preferrable.
    info = models.CharField(max_length=600)
    #TODO: why not just 'user'?
    user_no = models.OneToOneField(User, blank = True, null = True)
    #TODO: related_name?
    img = models.OneToOneField(Images, blank = True, null = True)
    
    def __unicode__(self):
         return u'Employee %s' % self.name

class Projects(models.Model):
    name = models.CharField(max_length=30)
    url_address = models.URLField()
    #TODO: TextField?
    info = models.CharField(max_length=50)
    date_start = models.DateField()
    #TODO: rename to 'client'
    klient = models.CharField(max_length=30)
    #TODO: rename to 'authors' or 'developers'
    autors = models.ManyToManyField(Employee)
    #TODO: What about screenshots?
    #TODO: add __unicode__

class Article(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now = True)
    #TODO: max value length for char field is 255
    text = models.CharField(max_length=600)
    #TODO: rename to 'author'
    #TODO: What if the same user writes several articles?
    autor = models.OneToOneField(Employee, blank = True, null = True)
    #TODO: fields of this type should be plural
    img = models.ManyToManyField(Images)

"""    
class Price(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
"""    
    
