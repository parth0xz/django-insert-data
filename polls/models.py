from django.db import models

# Create your models here.
class Parth(models.Model):
	name = models.TextField()
	surname = models.TextField()
	title = models.CharField(max_length=80)


