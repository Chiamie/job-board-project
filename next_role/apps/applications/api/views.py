


from rest_framework.views import APIView
from rest_framework.response import Response


from apps.jobs.models import JobListing
from apps.accounts.models import Resume
from apps.applications.models import Application

from apps.applications.services.application_service import (
    apply_to_job,
    update_application_status
)

from apps.applications.selectors.application_selector import (
    get_candidate_applications,
    get_employer_applications,
    get_application_by_id
)

from .serializers import (
    ApplicationSerializer,
    ApplySerializer,
    UpdateStatusSerializer
)


class ApplyToJobView(APIView):


    def post(self, request):
        serializer = ApplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        job = JobListing.objects.get(id=serializer.validated_data["job_id"])
        resume = Resume.objects.get(id=serializer.validated_data["resume_id"])

        application = apply_to_job(
            candidate=request.user.candidate_profile,
            job=job,
            resume=resume,
            cover_letter=serializer.validated_data.get("cover_letter", "")
        )

        return Response(ApplicationSerializer(application).data)


class CandidateApplicationsView(APIView):


    def get(self, request):
        apps = get_candidate_applications(request.user.candidate_profile)
        return Response(ApplicationSerializer(apps, many=True).data)


class EmployerApplicationsView(APIView):


    def get(self, request):
        apps = get_employer_applications(request.user.employer_profile)
        return Response(ApplicationSerializer(apps, many=True).data)


class UpdateApplicationStatusView(APIView):
   

    def patch(self, request, pk):
        serializer = UpdateStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        application = get_application_by_id(pk)

        if not application:
            return Response({"detail": "Not found"}, status=404)

        if application.job.employer != request.user:
            return Response({"detail": "Unauthorized"}, status=403)

        application = update_application_status(
            application,
            serializer.validated_data["status"]
        )

        return Response(ApplicationSerializer(application).data)


