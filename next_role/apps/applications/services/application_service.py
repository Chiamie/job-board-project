


from apps.applications.models import Application


def apply_to_job(candidate, job, resume, cover_letter=""):



    return Application.objects.create(
        candidate=candidate,
        job=job,
        resume=resume,
        cover_letter=cover_letter,
    )


def update_application_status(application, status):
    application.status = status
    application.save()
    return application