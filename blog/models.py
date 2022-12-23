from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
        

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
