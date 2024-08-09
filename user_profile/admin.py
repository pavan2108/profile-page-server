from django.contrib import admin

from .models.certification import Certification
from .models.experience import Experience
from .models.hackathon import Hackathon
from .models.project import Project
from .models.socials import Social


# Register your models here.

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('username', 'github', 'linkedin')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'description', 'link')


@admin.register(Hackathon)
class HackathonAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'year', 'achievements')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('username', 'company', 'designation', 'duration')


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'issuing_authority')
