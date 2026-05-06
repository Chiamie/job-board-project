

from django.contrib.auth import authenticate
from apps.accounts.models import User


def register_user(data):
    user = User.objects.create_user(
        email=data["email"],
        username=data["username"],
        password=data["password"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        phone_number=data["phone_number"],
        role=data.get("role", User.Role.CANDIDATE),
    )
    return user


def login_user(email, password):
    user = authenticate(username=email, password=password)
    if not user:
        raise Exception("Invalid credentials")
    return user