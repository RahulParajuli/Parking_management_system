from django.db import models

class Parkbay(models.Model):
    bay_number = models.IntegerField()
    bay_status = models.BooleanField(default=False)


    def __str__(self):
        return "Bay " + str(self.bay_number)