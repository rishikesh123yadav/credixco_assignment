from django.db import models
from django.utils import timezone

# Create your models here.
class SuperAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=200)
    admin_firstname = models.CharField(max_length=50)
    admin_lastname = models.CharField(max_length=50)
    admin_email = models.EmailField(max_length=50)
    admin_address = models.CharField(max_length=200)
    admin_phone = models.BigIntegerField()
    when_created = models.DateField(default=timezone.now)
    class Meta:
        db_table = 'adminDetails'

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=200)
    teacher_firstname = models.CharField(max_length=50)
    teacher_lastname = models.CharField(max_length=50)
    teacher_email = models.EmailField(max_length=50)
    teacher_address = models.CharField(max_length=200)
    teacher_phone = models.BigIntegerField()
    when_created = models.DateField(default=timezone.now)
    creator_adminId = models.CharField(max_length=50)
    class Meta:
        db_table = 'teacherDetails'

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=200)
    student_firstname = models.CharField(max_length=50)
    student_lastname = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=50)
    student_address = models.CharField(max_length=200)
    student_phone = models.BigIntegerField()
    when_created = models.DateField(default=timezone.now)
    create_by = models.CharField(max_length=50)
    creator_Id = models.CharField(max_length=50)
    class Meta:
        db_table = 'studentDetails'