from django.db import models


class ContactForm(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  subject = models.CharField(max_length=100)
  message = models.TextField()