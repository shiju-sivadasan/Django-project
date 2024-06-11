from django.urls import path
from .views import create_biography
urlpatterns = [
    path('',create_biography,name="create_bio")
]