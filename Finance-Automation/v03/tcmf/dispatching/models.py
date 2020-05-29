from django.db import models

# Create your models here.
class Trip(models.Model):
    # id field is automatically populated
    trip_no = models.IntegerField(null=False,blank=False)
    origin_city = models.CharField(max_length = 20, blank=False, null=False)
    destination_city = models.CharField(max_length = 20, blank=False, null=False)

    def __str__(self):
        return(f'Trip has been recoded as {self.trip_no} from {self.origin_city} to {self.destination_city}')