from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

##For Login in admin

class CustomerUser(AbstractUser):
    USER1 = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )
    user_type = models.CharField(choices=USER1, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')



class Courses(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class Session_year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + "-" + self.session_end



class Student(models.Model):
    admin = models.OneToOneField(CustomerUser, on_delete=models.CASCADE, blank=True)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_year, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.admin.first_name + "" + self.admin.last_name
