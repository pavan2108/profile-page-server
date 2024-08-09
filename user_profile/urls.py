from django.urls import path
from .views import (
    update_or_create_social,
    create_experience, update_experience, delete_experience,
    create_project, update_project, delete_project,
    create_hackathon, update_hackathon, delete_hackathon,
    create_certification, update_certification, delete_certification,
    get_profile
)

urlpatterns = [
    path('profiles/<str:username>/socials', update_or_create_social),
    path('profiles/<str:username>/experiences', create_experience),
    path('profiles/<str:username>/experiences/<int:id>', update_experience),
    path('profiles/<str:username>/experiences/<int:id>', delete_experience),
    path('profiles/<str:username>/projects', create_project),
    path('profiles/<str:username>/projects/<int:id>', update_project),
    path('profiles/<str:username>/projects/<int:id>', delete_project),
    path('profiles/<str:username>/hackathons', create_hackathon),
    path('profiles/<str:username>/hackathons/<int:id>', update_hackathon),
    path('profiles/<str:username>/hackathons/<int:id>', delete_hackathon),
    path('profiles/<str:username>/certifications', create_certification),
    path('profiles/<str:username>/certifications/<int:id>', update_certification),
    path('profiles/<str:username>/certifications/<int:id>', delete_certification),
    path('profiles/<str:username>', get_profile),
]
