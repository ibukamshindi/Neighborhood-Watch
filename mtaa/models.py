from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from django.dispatch import receiver



# Create your models here.
class Hood(models.Model):
    hood_name=models.CharField(max_length=50,blank=True)
    hood_photo=models.ImageField(upload_to='hoodpics/')
    population=models.CharField(max_length=50,blank=True)
class Profile(models.Model):
    name=models.CharField(max_length=50,blank=True)
    user_id=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Hood,null=True,on_delete=models.CASCADE)
    email_address=models.CharField(max_length=50,blank=True)

class Business(models.Model):
    business_name=models.CharField(max_length=50,blank=True)
    email=EmailField(null=False)
    user=models.ForeignKey(User,null=True,on_delete=models.Case)
    hood=models.ForeignKey(Hood,null=True,on_delete=models.CASCADE)

class Notification(models.Model):
    post=models.CharField(max_length=50,blank=True)
    posted_by=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    hood=models.ForeignKey(Hood,null=True,on_delete=models.CASCADE)
        

