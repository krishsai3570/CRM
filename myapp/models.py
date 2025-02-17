from django.db import models

from django.contrib.auth.models import User



class Customer(models.Model):

    name=models.CharField(max_length=200)

    email=models.EmailField()

    phone=models.CharField(max_length=50)

    address=models.TextField()

    created_at=models.DateTimeField(auto_now=True)

    updated_at=models.DateTimeField(auto_now=True)

    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)









































