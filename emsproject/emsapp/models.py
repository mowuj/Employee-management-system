from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image
from django.utils import timezone
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Post(models.Model):
    name=models.CharField(max_length = 150)

    def __str__(self):
        return self.name


class Division(models.Model):
    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name

class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Employee(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_id=models.CharField(max_length = 150, blank=True,null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    ssc = models.FloatField()
    hsc=models.FloatField(blank=True,null=True)
    honors=models.FloatField(blank=True,null=True)
    masters=models.CharField(max_length=250,blank=True,null=True)
    email =  models.EmailField()
    nid = models.IntegerField()
    selary= models.IntegerField()
    image = models.ImageField(default='default.jpg',upload_to='media/images')
    phone = models.CharField(max_length = 150)
    father_name = models.CharField(max_length = 150)
    mother_name = models.CharField(max_length = 150)

    def save(self,*args,**kwargs):
        super(Employee,self).save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            output_size=(200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)
    def __str__(self):
        return str(self.full_name)

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cause_of_leave = models.CharField(max_length = 250,blank = True,null=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    apply_date = models.DateField(auto_now_add=True)
    check_status=models.BooleanField(default=False)
    approve_status=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)
    
class Holiday(models.Model):
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    Description = models.CharField(max_length = 150)
    def __str__(self):
        return str(self.Description)

class DailyTask (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    description = models.TextField(blank=True,null=True)
    working_status=models.BooleanField(default=False)
    do_status=models.BooleanField(default=False)
    done_status=models.BooleanField(default=False)
    issue_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.user)

class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    meeting_date=models.DateField()
    meeting_time = models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.user)
    

class Attendence(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    attend_date = models.DateTimeField(default=timezone.now)
    on_time_status = models.BooleanField(default=False)
    late_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

class Client(models.Model):
    client_name = models.CharField(max_length=250)
    client_id=models.CharField(max_length = 150, blank=True,null=True)
    company_name = models.CharField(max_length=250)
    email =  models.EmailField()
    nid = models.IntegerField()
    image = models.ImageField(default='default.jpg',upload_to='media/images')
    phone = models.CharField(max_length = 150)
    
    def __str__(self):
        return str(self.client_name)
