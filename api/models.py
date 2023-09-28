from django.db import models

# Create your models here.

# Model for Course
class Courses(models.Model):
    course_id = models.AutoField(primary_key=True) # Primary Key
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    fees = models.IntegerField()

    def __str__(self):
        return self.title
    


choose_gender = (
    ('Male', 'male'),
    ('Female','female'),
    ('OTHER', 'other'),
)

# Model for Student
class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    gender = models.CharField(max_length=8, choices=choose_gender, default="MALE")
    city = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    date_enrolled = models.DateTimeField(auto_now_add=True)
    courses = models.ForeignKey('Courses', on_delete=models.CASCADE, related_name='enrolled')

    def __str__(self):
        return self.name+'--'+self.city

    

