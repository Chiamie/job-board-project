

from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank
from apps.jobs.models import JobListing


def filter_jobs(
    keyword=None,
    location=None,
    job_type=None,
    min_salary=None,
    max_salary=None,
    category_id=None,
    is_remote=None,
):
    query_selector = JobListing.objects.filter(is_active=True)

    # 🔍 Full-text search
    if keyword:
        search_query = SearchQuery(keyword)
        query_selector = query_selector.annotate(
            rank=SearchRank("search_vector", search_query)
        ).filter(rank__gte=0.1).order_by("-rank")

    if location:
        query_selector = query_selector.filter(location__icontains=location)

    if job_type:
        query_selector = query_selector.filter(job_type=job_type)

    if min_salary:
        query_selector = query_selector.filter(salary_max__gte=min_salary)

    if max_salary:
        query_selector = query_selector.filter(salary_min__lte=max_salary)

    if category_id:
        query_selector = query_selector.filter(category_id=category_id)

    if is_remote is not None:
        query_selector = query_selector.filter(is_remote=is_remote)

    return query_selector