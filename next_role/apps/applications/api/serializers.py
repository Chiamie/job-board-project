


from rest_framework import serializers
from apps.applications.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"


class ApplySerializer(serializers.Serializer):
    job_id = serializers.IntegerField()
    resume_id = serializers.IntegerField()
    cover_letter = serializers.CharField(required=False, allow_blank=True)


class UpdateStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Application.Status.choices)