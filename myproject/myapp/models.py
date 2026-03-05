from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
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
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use Django's password hashing
    name = models.CharField(max_length=50)  # Increased length for more flexibility
    teacher_class = models.PositiveIntegerField()  # Ensuring only positive numbers
    subject = models.CharField(max_length=50)  # Increased length for more flexibility
    ph_number = models.CharField(
        max_length=10,  # Max length considering international formats
        validators=[
            MinLengthValidator(10),
            RegexValidator(r'^\d{10,15}$', message="Phone number must be between 10 and 15 digits.")
        ]
    )
    def __str__(self):
      return self.name