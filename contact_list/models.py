from django.db import models

# Create your models here.
class People(models.Model):
    people_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=11)
    note = models.TextField()

    def __str__(self):
        return self.name
