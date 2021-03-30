from django.db import models

class HospitalModel(models.Model):
    hospital_name = models.CharField(max_length = 100)
    critical_level = models.CharField(max_length = 100)
    pin_code = models.IntegerField()
    date_slot = models.DateField(null=True)
    time_slot = models.TimeField()

    beds = models.IntegerField(default=1)

    def __str__(self):
        return self.hospital_name

    
    
    
