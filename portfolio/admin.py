from django.contrib import admin
from .models import Project

# Register your models here.
# Class to show the read-only fields of the table 
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)