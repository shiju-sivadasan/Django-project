from django.urls import path
from .views import create_details
urlpatterns = [
    path('create_details',create_details,name="create_details")
]