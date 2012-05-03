from django.db import models
from django.contrib.auth.models import User
import os.path

class Base(models.Model):
    #TODO: How are you going to get this user from db? 
    created_by = models.CharField(max_length=30, blank = True, null = True)
    created_at = models.DateField(auto_now_add = True, blank = True, null = True)
    modified_by = models.CharField(max_length=30, blank = True, null = True)
    modified_at = models.DateField(auto_now = True, blank = True, null = True)
	
    class Meta:
        abstract = True

class Image(Base):    
    title = models.CharField(max_length=60)
    url = models.ImageField(upload_to=os.path.join(os.path.dirname(__file__),'img').replace('\\','/'), blank = True, null = True)

class Employee(Base):
    name = models.CharField(max_length=30)
    #address = models.CharField(max_length=50)
    skype = models.CharField(max_length=20, blank = True, null = True)
    jabber = models.CharField(max_length=20, blank = True, null = True)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField(blank = True, null = True)
    position_in_team = models.CharField(max_length=60, blank = True, null = True)
    education = models.CharField(max_length=60)
    skills = models.CharField(max_length=60, blank = True, null = True)
    info = models.TextField()
    user = models.OneToOneField(User, related_name = 'employee', blank = True, null = True)
    img = models.OneToOneField(Image, related_name = 'employee', blank = True, null = True)
    
    def __unicode__(self):
         return u'Employee %s' % self.name

class Projects(Base):
    name = models.CharField(max_length=30)
    url_address = models.URLField()
    info = models.TextField()
    date_start = models.DateField()
    client = models.CharField(max_length=30, blank = True, null = True)
    authors = models.ManyToManyField(Employee, related_name = 'projects')
    screenshots = models.ManyToManyField(Image, related_name = 'projects')

    def __unicode__(self):
        #TODO: fix incorrect string
        return u'Employee %s' % self.name

class Article(Base):
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now = True)
    text = models.TextField()
    #TODO: What if the same user writes several articles? your fix is not correct
    author = models.OneToOneField(Employee, related_name = 'article', blank = True, null = True)
    #TODO: fields of this type should be plural. your fix is not correct
    img = models.OneToOneField(Image, related_name = 'article', blank = True, null = True)

"""    
class Price(Base):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
"""    
    
