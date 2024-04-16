from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        error_messages={
            'invalid': 'Please enter a valid email address.',
        }
    )
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name