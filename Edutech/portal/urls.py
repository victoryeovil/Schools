from django.urls import path
from .views import *

urlpatterns = [
    path('student_profile/', student_profile, name="student profile"),
]
