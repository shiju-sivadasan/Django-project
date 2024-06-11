from django.urls import path
from .views import create_project_details,portfolio
urlpatterns = [
    path('create_proj_details',create_project_details,name="create_project_details"),
    path('portfolio',portfolio,name="portfolio"),
]