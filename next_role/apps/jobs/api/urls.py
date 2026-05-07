


from django.urls import path
from .views import JobListView, CreateJobView

urlpatterns = [
    path("", JobListView.as_view()),
    path("create/", CreateJobView.as_view()),
]