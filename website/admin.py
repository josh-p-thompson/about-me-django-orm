from django.contrib import admin

# Register your models here.
from .models import About, Project
admin.site.register(About)
admin.site.register(Project)