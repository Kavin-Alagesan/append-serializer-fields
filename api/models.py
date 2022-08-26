from django.db import models

# Create your models here.
class OfficeModel(models.Model):
    designation=models.CharField(max_length=30)
    department=models.CharField(max_length=30)

    def __str__(self):
        return "{self.designation}:{self.department}"

