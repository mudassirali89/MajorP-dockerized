from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=15)  # Update max_length to match the database
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class student_marks_model(models.Model):

    regno=models.CharField(max_length=300)
    names=models.CharField(max_length=300)
    sem1=models.CharField(max_length=300)
    sem2=models.CharField(max_length=300)
    sem3=models.CharField(max_length=300)

class StudentMarksModel(models.Model):
    # Define the fields for the model
    student_name = models.CharField(max_length=255)
    marks = models.IntegerField()
    risk_status = models.CharField(max_length=50)
    # Add other fields as necessary

    def __str__(self):
        return self.student_name

class student_risk_prediction_model(models.Model):

    regno = models.CharField(max_length=300)
    names = models.CharField(max_length=300)
    sem1 = models.CharField(max_length=300)
    sem2 = models.CharField(max_length=300)
    sem3 = models.CharField(max_length=300)
    avg= models.CharField(max_length=300)
    risk= models.CharField(max_length=300)

class detection_ratio_model(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)


