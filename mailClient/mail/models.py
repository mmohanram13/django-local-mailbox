from django.db import models

class Email(models.Model):
    user_email = models.CharField(max_length=20)
    recipient_email = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True) 