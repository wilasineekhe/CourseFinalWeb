from django.db import models
from django.contrib.auth.models import User
from app_user.models import User_info

# Create your models here.

class Course(models.Model):
    Title = models.CharField(max_length= 60)
    code = models.CharField(max_length=15,null=True,blank=True)
    image = models.ImageField(upload_to='general_APP/files/covers',blank=True)
    lecturer = models.CharField(max_length=60,null=True,blank=True)
    Info = models.TextField(null= True,blank=True)
    Date_open = models.DateTimeField(null=True)
    Date_close = models.DateTimeField(null=True)
    Is_open = models.BooleanField(default=True)
    Is_full = models.BooleanField(default=False)
    Enroll_by_user_info = models.ManyToManyField(
        to = User_info,
        through= 'general_APP.Enrollment',
        related_name='Enroll_in_course',
        )
    
    
    def __str__(self) -> str:
        return '{} (id = {})'.format(self.Title, self.id)
    
class Enrollment(models.Model):
    Is_pass = models.BooleanField(default=False)
    enroll_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_user_info = models.ForeignKey(User_info, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '(id = {}) user: {} {} '.format(self.id,self.enroll_user_info.first_name ,self.enroll_user_info.last_name)
    

