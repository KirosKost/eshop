from django.db import models
from django.urls import reverse
from datetime import datetime



class Blog(models.Model):
	title = models.CharField(max_length=20)
	img =models.ImageField(null=True, blank=True, upload_to='images/')
	describe= models.CharField(max_length=350)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title