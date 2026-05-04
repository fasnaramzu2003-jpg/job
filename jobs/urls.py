from django.urls import path
from .views import job_list, job_detail

urlpatterns = [
    path('jobs/', job_list),              # GET, POST
    path('jobs/<int:pk>/', job_detail),   # GET, PUT, DELETE
]