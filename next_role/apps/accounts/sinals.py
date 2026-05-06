

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import CandidateProfile, EmployerProfile, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.Role.CANDIDATE:
            CandidateProfile.objects.create(user=instance)
        elif instance.role == User.Role.EMPLOYER:
            EmployerProfile.objects.create(user=instance)