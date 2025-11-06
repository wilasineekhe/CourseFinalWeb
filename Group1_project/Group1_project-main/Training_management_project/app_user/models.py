from django.db import models
from django.contrib.auth.models import User,UserManager

# Create your models here.
class User_info(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=60,null=True,blank=True)
    last_name = models.CharField( max_length=60,null=True,blank=True)
    email = models.CharField( max_length=255,blank=True,null=True)
    student_ID = models.CharField(max_length=50,blank=True,null=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    def __str__(self) -> str:
        return '{} (id = {})'.format(self.first_name, self.id)

    
