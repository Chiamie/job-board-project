


from django.urls import path
from .views import (
    ApplyToJobView,
    CandidateApplicationsView,
    EmployerApplicationsView,
    UpdateApplicationStatusView
)

urlpatterns = [
    path("apply/", ApplyToJobView.as_view()),
    path("candidate/", CandidateApplicationsView.as_view()),
    path("employer/", EmployerApplicationsView.as_view()),
    path("<int:pk>/status/", UpdateApplicationStatusView.as_view()),
]