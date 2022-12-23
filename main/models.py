from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = PhoneNumberField(default=None, null=False, blank=True, unique=True)
    description = models.TextField()
    sent = models.DateTimeField(auto_now=True)