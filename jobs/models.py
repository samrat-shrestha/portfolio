from django.db import models

# Create your models here.
# models.Model allows job class to be connected to the database.
class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)

	# def __str__(self):
	# 	return self.summary


