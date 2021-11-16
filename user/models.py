from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
GENDER=[
    ("M","Male"),
    ("F", "Female")
]
class UserAccount(models.Model):
	name 					= models.CharField(max_length=50, null=False, blank=False)
	family 					= models.CharField(max_length=50, null=False, blank=False)
	phonenumber 			= models.CharField(max_length=50, null=False, blank=False)
	birthdate 				= models.CharField(max_length=50, null=False, blank=False)
	gender 					= models.CharField(max_length=2, choices=GENDER)    
	address 				= models.TextField(max_length=500, null=False, blank=False)
	date_published 			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 			= models.DateTimeField(auto_now=True, verbose_name="date updated")


	def __str__(self):
		return self.name + ' ' + self.family
