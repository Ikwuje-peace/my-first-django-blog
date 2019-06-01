from django.db import models

# Create your models here.
class Post(models.Model):
	title 		= models.CharField(max_length=120)
	body 	 	= models.TextField()
	author	 	= models.CharField(max_length=120)
	active      = models.BooleanField(default=True)
	published 	= models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
	post = models.TextField()
	author = models.TextField()
	body = models.TextField(default='Write a post')
