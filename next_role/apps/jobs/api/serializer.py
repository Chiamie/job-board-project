


from rest_framework import serializers
from apps.jobs.models import JobListing


class JobSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = "__all__"


class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        exclude = ["employer", "search_vector", "created_at"]