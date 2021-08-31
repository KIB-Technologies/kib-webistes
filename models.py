from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.utils import timezone
from datetime import datetime

class Blog(models.Model):
    blog_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    blogshortdes = models.CharField(max_length=400, blank=True, null=True)  
    bloghiglight = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images/blogs")
    imagealt = models.CharField(max_length=60, blank=True, null=True)
    source = models.CharField(max_length=40, blank=True, null=True)
    source_link = models.URLField(blank=True,null=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return(self.title)



class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()

    class Meta:
        verbose_name="Query"
        verbose_name_plural="Queries"

    def __str__(self):
        return(self.name)