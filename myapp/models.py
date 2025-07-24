from django.db import models
class Visitor(models.Model):
    visitor_id = models.PositiveIntegerField(unique=True)  # Unique ID
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    category = models.CharField(max_length=50)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()
    designated_attendee = models.CharField(max_length=100)

    def _str_(self):
        return self.visitor_name

