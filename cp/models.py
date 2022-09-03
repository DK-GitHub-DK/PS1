from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):

    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    hostel = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    room_no = models.IntegerField()

class Complaint(models.Model):

    student = models.ForeignKey(Student, on_delete = models.CASCADE)

    category_choices = (
        ('housekeeping','housekeeping'),
        ('security', 'security'),
        ('geenral', 'general')
        )
    category = models.CharField(choices=category_choices, max_length=100)
    description = models.TextField()
    photo = models.ImageField(null = True, blank = True)

