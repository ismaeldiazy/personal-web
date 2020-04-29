from django.db import models

# Project model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects")
    link = models.URLField(null=True, blank=True)
    # Created date
    created = models.DateTimeField(auto_now_add=True)
    # Modification date 
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # Ordered by created date (from new to old)
        ordering = ["-created"]
    # Give to the instantiation the title name
    def __str__(self):
        return self.title
