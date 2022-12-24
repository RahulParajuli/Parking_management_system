from django.db import models
from datetime import datetime

class BayBooking(models.Model):
    name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    booking_date = models.DateTimeField(default=datetime.utcnow, blank=True)
    booking_for = models.DateField(null=False)
    booking_status = models.BooleanField(default=False)
    booked_bay_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name + "-- LIS NO. - " + self.license_plate + "-- Booking Date. - " + str(self.booking_for) + " -- Bay Allocated - " + str(self.booked_bay_number)

class Parkbay(models.Model):
    bay_id = models.IntegerField(auto_created=True, null=False, primary_key=True)
    bay_number = models.IntegerField(default=0)
    booked = models.BooleanField(default=False)
    date = models.DateField(default=datetime.today, blank=True)
    
    def __str__(self):
        return "Bay " + str(self.bay_number)+  "     " + "Booking Date" + "   " + str(self.date)

    def flush(self):
        if self.date < datetime.now():
            self.booked = False
            self.save()