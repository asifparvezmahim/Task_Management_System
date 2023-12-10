from django.db import models
from category.models import Category


# Create your models here.
class Task(models.Model):
    Task_Title = models.CharField(max_length=30)
    Task_Description = models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_Assign_Date = models.DateTimeField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.Task_Title
