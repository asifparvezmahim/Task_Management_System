from django.db import models


# Create your models here.
class Category(models.Model):
    Category_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_Name
