from django.db import models

# Create your models here.
class Filters(models.Model):
	kind = models.CharField(max_length=1)
	name = models.CharField(max_length=100)
	label = models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Games(models.Model):
	app_id = models.IntegerField(max_digits=10)
	app_name = models.CharField(max_length=100)
	metascore = models.IntegerField(max_digits=3)
	def __str__(self):
		return self.app_name
class Index(models.Model):
	kind = models.CharField(max_length=1)
	name = models.CharField(max_length=100)
	app_id = models.IntegerField(max_digits=10)
	def __str__(self):
		return self.name