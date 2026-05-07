import uuid

from django.db import models
from django.conf import settings
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField

from apps.accounts.models import EmployerProfile


class JobCategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )

    class Meta:
        unique_together = ("name", "parent")

    def __str__(self):
        return self.name

class JobListing(models.Model):
    class JobType(models.TextChoices):
        FULL_TIME = "full_time", "Full-time"
        PART_TIME = "part_time", "Part-time"
        CONTRACT = "contract", "Contract"
        INTERNSHIP = "internship", "Internship"

    employer = models.ForeignKey(
        EmployerProfile,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    category = models.ForeignKey(
        JobCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="jobs"
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=False, blank=False)
    requirements = models.TextField(max_length=500, null=False, blank=False)

    location = models.CharField(max_length=255)
    is_remote = models.BooleanField(default=False)

    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    job_type = models.CharField(max_length=20, choices=JobType.choices)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # 🔍 PostgreSQL full-text search
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=["search_vector"]),
            models.Index(fields=["location"]),
            models.Index(fields=["job_type"]),
            models.Index(fields=["is_active"]),
        ]

    def __str__(self):
        return self.title