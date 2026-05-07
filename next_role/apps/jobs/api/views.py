


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from apps.jobs.services.job_services import create_job
from apps.jobs.selectors.job_selectors import filter_jobs

from .serializer import JobSearchSerializer, CreateJobSerializer


class JobListView(APIView):
    def get(self, request):
        jobs = filter_jobs(
            keyword=request.GET.get("keyword"),
            location=request.GET.get("location"),
            job_type=request.GET.get("job_type"),
            min_salary=request.GET.get("min_salary"),
            max_salary=request.GET.get("max_salary"),
            category_id=request.GET.get("category_id"),
            is_remote=request.GET.get("is_remote"),
        )
        return Response(JobSearchSerializer(jobs, many=True).data)


class CreateJobView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CreateJobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        job = create_job(
            employer=request.user.employer_profile,
            data=serializer.validated_data
        )

        return Response(JobSearchSerializer(job).data)