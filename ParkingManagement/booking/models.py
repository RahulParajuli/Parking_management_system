from django.db import models

class Booking(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    bay = models.ForeignKey('carpark.Parkbay', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booking_status = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.name + " " + str(self.bay.bay_number)
