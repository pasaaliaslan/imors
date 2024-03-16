from json import loads

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, JsonResponse
from django.middleware.csrf import get_token
from django.views import View
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from imors_auth.models import User
from imors_auth.serializers import UserSerializer
from util.views import validate_params


class CsrfView(View):
    def get(self, request: HttpRequest):
        csrf_token = get_token(request)

        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key

        return JsonResponse({"csrf_token": csrf_token, "session_id": session_id})


class RegisterView(View):
    @validate_params(
        required_body_params={
            "username": str,
            "email": str,
            "password": str,
        }
    )
    def post(self, request: HttpRequest):
        data = loads(request.body)
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        if User.objects.filter(username=username).exists():
            return HttpResponse("User already exists.", status=HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse("User is registered", status=HTTP_201_CREATED)


class LoginView(View):
    @validate_params(
        required_body_params={
            "username": str,
            "password": str,
        }
    )
    def post(self, request: HttpRequest):
        data = loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse()
        else:
            return HttpResponseForbidden()


class SessionView(View, LoginRequiredMixin):
    def get(request: HttpRequest):
        user = request.user

        if user.is_authenticated:
            return HttpResponse(UserSerializer(user).data)

        else:
            return HttpResponseForbidden("User is not authenticated.")


class LogoutView(View, LoginRequiredMixin):
    def get(request: HttpRequest):
        logout(request)
        return HttpResponse()
