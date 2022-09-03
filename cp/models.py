from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):

    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)

    hostel_choices = (
        ('alakananda','Alakananda'),
        ('brahmaputra', 'Brahmaputra'),
        ('cauvery', 'Cauvery'),
        ('ganga','Ganga'),
        ('godaveri','Godaveri'),
        ('jamuna', 'Jamuna'),
        ('krishna', 'Krishna'),
        ('mahanadhi', 'Mahanadhi'),
        ('mandakini_a', 'Mandakini A'),
        ('mandhakini_b', 'Mandakini B'),
        ('narmada', 'Narmada'),
        ('pampa', 'Pampa'),
        ('saraswathi', 'Saraswathi'),
        ('sindhu', 'Sindhu'),
        ('tamiraparani', 'Tamiraparani'),
        ('tapti', 'Tapti'),
        ('bhadra', 'Bhadra'),
        ('sabarmati', 'Sabarmati'),
        ('sarayu', 'Sarayu'),
        ('sharavathi', 'Sharavathi'),
        ('tunga', 'Tunga')
    )
    hostel = models.CharField(choices = hostel_choices,max_length=100)
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    room_no = models.IntegerField()

    def __str__(self):
        return self.name

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

