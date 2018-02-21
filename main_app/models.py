from django.db import models


from django.contrib.auth.models import User

# Create your models here.
class Filter(models.Model):
	kind = models.CharField(max_length=1)
	name = models.CharField(max_length=100)
	label = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Game(models.Model):
	app_id = models.IntegerField()
	app_name = models.CharField(max_length=100)
	metascore = models.IntegerField()
	def __str__(self):
		return self.app_name

class Index(models.Model):
	kind = models.CharField(max_length=1)
	name = models.CharField(max_length=100)
	app_id = models.IntegerField()
	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
