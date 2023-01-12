from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    