from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(AbstractUser):
    User_type_choices = (
        ('recruiter', 'Recruiter'),
        ('jobseeker', 'Jobseeker')
    )
    user_type = models.CharField(choices=User_type_choices,max_length=50)
    display_name = models.CharField(max_length=255)

class JobPost(models.Model):
    CATEGORY_CHOICES = (
        ('IT', 'Information Technology'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        
    )

    title = models.CharField(max_length=100)
    number_of_openings = models.IntegerField()
    job_description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    recruiter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    jobseeker = models.ManyToManyField(CustomUser, related_name='job_applications', blank=True)

class JobApplication(models.Model):
    job_post = models.ForeignKey('JobPost', on_delete=models.CASCADE)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.applicant.username} - {self.job_post.title}"