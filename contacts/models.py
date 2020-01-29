from django.db import models
from datetime import datetime

class Contact(models.Model):
  product_title = models.CharField(max_length=200)
  service_title = models.CharField(max_length=200)
  product_id = models.IntegerField()
  service_id = models.IntegerField(blank=True, null=True)
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name

class Contact_us(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name

