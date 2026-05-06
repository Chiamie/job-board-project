import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    class Role(models.TextChoices):
        CANDIDATE = "candidate", "Candidate"
        EMPLOYER = "employer", "Employer"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CANDIDATE
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    phone_number = models.CharField(max_length=11, null=False, blank=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def is_employer(self):
        return self.role == self.Role.EMPLOYER

    def is_candidate(self):
        return self.role == self.Role.CANDIDATE





class CandidateProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="candidate_profile"
    )

    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"CandidateProfile({self.user})"

class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    candidate = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE,
        related_name="resumes"
    )

    title = models.CharField(max_length=255, blank=True)
    is_default = models.BooleanField(default=False)
    file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume({self.candidate})"

class EmployerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employer_profile"
    )

    company_name = models.CharField(max_length=255)
    company_description = models.TextField(blank=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"Profile for {self.company_name}"