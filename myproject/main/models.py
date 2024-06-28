from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=10,unique=True)
    is_doctor = models.BooleanField('Is doctor', default=False)
    is_patient = models.BooleanField('Is patient', default=False)

class Files(models.Model):
    test_type = models.CharField(max_length=20)
    file = models.FileField(upload_to='pdfs/')
    uploaded_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='uploaded_files')

    def __str__(self):
        return f"{self.test_type} uploaded by {self.uploaded_by.username} on {self.uploaded_date}"
    

class Labfiles(models.Model):
    testtype = models.CharField(max_length=20)
    lab_file = models.FileField(upload_to='pdfs/')
    uploaded_date = models.DateTimeField(auto_now_add=True)
    uploaded_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='uploaded_labfiles')

    def __str__(self):
        return f"{self.testtype} uploaded by {self.uploaded_user.username} on {self.uploaded_date}"
    
class Appointment(models.Model):
    docterName = models.CharField(max_length=20)
    patientName = models.CharField(max_length=20)
    appointmentDate = models.DateField(auto_now_add=True)
    appointmentTime = models.TimeField(auto_now_add=True)
    reason = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.docterName} - {self.patientName} on {self.appointmentDate}"
