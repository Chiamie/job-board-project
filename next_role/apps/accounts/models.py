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