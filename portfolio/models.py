from django.db import models

# Project model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    # Created date
    created = models.DateTimeField(auto_now_add=True)
    # Modification date 
    updated = models.DateTimeField(auto_now=True)
