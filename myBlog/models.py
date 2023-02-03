from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #redirect to the article
        #return reverse('article-detail', args=(str(self.id)) )
        #redirect to the homepage
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True, null=True, upload_to="images/profile/")
    facebook_url = models.CharField(max_length=255, blank=True, null=True,)
    twitter_url = models.CharField(max_length=255, blank=True, null=True,)
    tiktok_url = models.CharField(max_length=255, blank=True, null=True,)
    linkedIn_url = models.CharField(max_length=255, blank=True, null=True,)



    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(blank=True, null=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #redirect to the article
        #return reverse('article-detail', args=(str(self.id)) )

        #redirect to the homepage
        return reverse('home')
