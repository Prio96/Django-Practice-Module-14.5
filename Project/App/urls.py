from django.urls import path
from .views import viewform
urlpatterns = [
    path('form/',viewform,name="form")
]