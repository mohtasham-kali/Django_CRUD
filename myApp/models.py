from django.db import models

# Create your models here.

class Students(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName