from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)
    age=models.CharField(max_length=20)
    address=models.TextField()

    def __str__(self):
        return str(self.name)
    

class Employee(models.Model):
    depat_choice=(
        ('IT','IT'),
        ('NON IT','NON IT'),
    )
    student=models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,blank=True,related_name='employee_student')
    department=models.CharField(max_length=23,choices=depat_choice,null=True,blank=True)
    name=models.CharField(max_length=23,null=True,blank=True)

    def __str__(self):
        return str(self.name)