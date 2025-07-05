from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    soil_moisture = models.IntegerField()
    water_level = models.IntegerField()
    irrigation_status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.timestamp} - Moisture: {self.soil_moisture}%"
