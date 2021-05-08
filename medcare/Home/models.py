from django.db import models

# Create your models here.

class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    Name = models.CharField(blank=False, max_length = 30)
    Desgination = models.CharField(blank=False, max_length = 30)
    Qulaitfication = models.CharField(blank=False, max_length = 30)
    Hospital = models.CharField(blank=False, max_length = 30)
    is_online = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name