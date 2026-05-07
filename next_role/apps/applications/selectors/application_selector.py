


from apps.applications.models import Application


def get_candidate_applications(candidate):
    return Application.objects.filter(candidate=candidate).select_related("job")


def get_employer_applications(employer):
    return Application.objects.filter(
        job__employer=employer
    ).select_related("candidate", "job")


def filter_applications_by_status(queryset, status):
    if status:
        return queryset.filter(status=status)
    return queryset

def get_application_by_id(pk):
    try:
        return Application.objects.get("candidate", "job").get(id=pk)
    except Application.DoesNotExist:
        return None


