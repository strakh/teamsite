from django.db import models
from django.contrib.auth.models import User
import os.path

#TODO: What about base model for created_by/created_at as we discussed?
class Base(models.Model):
    created_by = models.CharField(max_length=30, blank = True, null = True)
    created_at = models.DateField(auto_now_add = True, blank = True, null = True)
    modified_by = models.CharField(max_length=30, blank = True, null = True)
    modified_at = models.DateField(auto_now = True, blank = True, null = True)
	
    class Meta:
        abstract = True

#(SOLVED)TODO: class name should be singlular
class Image(Base):    
    title = models.CharField(max_length=60)
    #(SOLVED)TODO: ImageField is better here. 
    url = models.ImageField(upload_to=os.path.join(os.path.dirname(__file__),'img').replace('\\','/'), blank = True, null = True)

class Employee(Base):
    name = models.CharField(max_length=30)
    #(SOLVED)TODO: Not sure we really need team member's address here, 
    # but we really need more contact info like skype or jabber
    #address = models.CharField(max_length=50)
    skype = models.CharField(max_length=20, blank = True, null = True)
    jabber = models.CharField(max_length=20, blank = True, null = True)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    #(SOLVED)TODO: What is date? birth date?
    birth_date = models.DateField(blank = True, null = True)
    #(SOLVED)TODO: Not sure I understand what is it? maybe position in team?
    # This is 
    position_in_team = models.CharField(max_length=60, blank = True, null = True)
    education = models.CharField(max_length=60)\
    #(SOLVED)TODO: rename this to 'skills'
    skills = models.CharField(max_length=60, blank = True, null = True)
    #(SOLVED)TODO: i think TextField is preferrable.
    info = models.TextField()
    #(SOLVED)TODO: why not just 'user'?
    user = models.OneToOneField(User, related_name = 'employee', blank = True, null = True)
    #(SOLVED)TODO: related_name?
    img = models.OneToOneField(Image, related_name = 'employee', blank = True, null = True)
    
    def __unicode__(self):
         return u'Employee %s' % self.name

class Projects(Base):
    name = models.CharField(max_length=30)
    url_address = models.URLField()
    #(SOLVED)TODO: TextField?
    info = models.TextField()
    date_start = models.DateField()
    #(SOLVED)TODO: rename to 'client'
    client = models.CharField(max_length=30, blank = True, null = True)
    #(SOLVED)TODO: rename to 'authors' or 'developers'
    authors = models.ManyToManyField(Employee, related_name = 'projects')
    #(SOLVED)TODO: What about screenshots?
    #(SOLVED)TODO: add __unicode__
    screenshots = models.ManyToManyField(Image, related_name = 'projects')

    def __unicode__(self):
         return u'Employee %s' % self.name

class Article(Base):
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now = True)
    #(SOLVED)TODO: max value length for char field is 255
    text = models.TextField()
    #(SOLVED)TODO: What if the same user writes several articles?
    author = models.OneToOneField(Employee, related_name = 'article', blank = True, null = True)
    #(SOLVED)TODO: fields of this type should be plural
    img = models.OneToOneField(Image, related_name = 'article', blank = True, null = True)

"""    
class Price(Base):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
"""    
    
