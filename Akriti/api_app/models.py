from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_reg_no = models.IntegerField()
    student_branch = models.CharField(max_length=20)
    student_batch = models.CharField(max_length=10)
