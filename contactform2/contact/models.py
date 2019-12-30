from django.db import models

# Create your models here.
class contact(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	telephone = models.CharField(max_length = 50)
	note = models.CharField(max_length = 50)
	company_name = models.CharField(max_length = 50)
	date_created = models.DateTimeField(auto_now_add = True)
	last_modified = models.DateTimeField(auto_now = True)