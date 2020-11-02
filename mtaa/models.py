from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from django.dispatch import receiver



# Create your models here.
class Hood(models.Model):
    hood_name=models.CharField(max_length=50,blank=True)
    hood_photo=models.ImageField(upload_to='hoodpics/')
    population=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.hood_name

    def create_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    def find_neighborood(self,hood_id):
        self.search_by_id(id=hood_id)

    def update_neighborhood(self):
        self.update_hood()
    
    def update_occupants(self):
        self.update_population()
        
class Profile(models.Model):
    name=models.CharField(max_length=50,blank=True)
    user_id=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Hood,null=True,on_delete=models.CASCADE)
    email_address=models.CharField(max_length=50,blank=True)

    def __str__(self):
      return self.name
    
    def save_user(self):
        self.save()

    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    def save_profile(sender,instance,**kwargs):
        instance.profile.save()    
class Business(models.Model):
    business_name=models.CharField(max_length=50,blank=True)
    email=EmailField(null=False)
    user=models.ForeignKey(User,null=True,on_delete=models.Case)
    hood=models.ForeignKey(Hood,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.hood

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(self,business_id):
        self.search_by_id(id=business_id)

    def update_business(self):
        self.update()

    

class Notification(models.Model):
    post=models.CharField(max_length=50,blank=True)
    posted_by=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    hood=models.ForeignKey(Hood,null=True,on_delete=models.CASCADE)
        

