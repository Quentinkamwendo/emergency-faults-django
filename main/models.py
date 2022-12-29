from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    sent = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-sent']
