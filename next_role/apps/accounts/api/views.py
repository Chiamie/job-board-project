from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from serializer import RegisterSerializer, LoginSerializer, UserSerializer
from apps.accounts.services.auth_service import register_user, login_user


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = register_user(serializer.validated_data)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = login_user(
            serializer.validated_data["email"],
            serializer.validated_data["password"]
        )

        return Response(UserSerializer(user).data)