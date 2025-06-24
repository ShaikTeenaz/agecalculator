from datetime import date
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def calculate_age(self):
        today = date.today()
        dob = self.date_of_birth
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def __str__(self):
        return self.name
