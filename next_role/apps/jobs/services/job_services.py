


from apps.jobs.models import JobListing


def create_job(employer, data):
    return JobListing.objects.create(
        employer=employer,
        title=data["title"],
        description=data["description"],
        location=data["location"],
        job_type=data["job_type"],
        salary_min=data.get("salary_min"),
        salary_max=data.get("salary_max"),
        category_id=data.get("category_id"),
        is_remote=data.get("is_remote", False),
    )