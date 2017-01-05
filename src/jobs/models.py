from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.
class Jobs(models.Model):
	title = models.CharField(max_length=150)
	company = models.CharField(max_length=150)
	salary = models.CharField(max_length=150)
	description = models.TextField()
	date_posted = models.DateField(("Date"), default=datetime.date.today)
