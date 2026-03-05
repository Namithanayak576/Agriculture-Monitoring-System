from django.db import models

class Student(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    student_class = models.CharField(max_length=10)
    section=models.CharField(max_length=2,default='A')
    phone_number = models.CharField(max_length=15)  # Ensure enough length for phone numbers
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    teacher_class = models.IntegerField()
    section = models.CharField(max_length=5,default='A')  # Add this field
    subject = models.CharField(max_length=20)
    ph_number = models.IntegerField()

    def __str__(self):
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

from .models import Student, Subject

class Grade(models.Model):
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()
    grade_date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.score}"


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    

    def __str__(self):
        return self.title
