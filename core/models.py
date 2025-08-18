from django.db import models
from datetime import date
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    education = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    bio_summary = models.TextField(blank=True, null=True)
    gender = models.CharField(
        choices=(
            ('male', "Male"),
            ('female', "Female"),
            ('other', "Other"),
        ),
        default="female",
        max_length=10
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Experience(models.Model):
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    company_location = models.CharField(max_length=50)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(blank=True, null=True,default=date.today)
    job_description = models.TextField()

    def __str__(self):
        return f"{self.job_title}  at {self.company}"

    
class Education(models.Model):
    institution_name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=50, blank=True, null= True)

    def __str__(self):
        return f"{Student().first_name} education"

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.TextField()
    technologies = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    link = models.CharField(max_length=50, null=True, blank=True)
    achievements = models.CharField(max_length=50, null=True, blank=True) 


    def __str__(self):
        return f"{Student().first_name} {self.project_name}"