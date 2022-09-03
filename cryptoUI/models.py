from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class SignUp(models.Model):
    name = models.CharField(max_length=30)
    Username = models.ForeignKey(login, on_delete=models.CASCADE)
    email_id = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
