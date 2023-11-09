from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from .utils import exact_response_data, get_url_response

BASE_URL = "https://ghibliapi.vercel.app/films"


class ActorViewSet(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60))
    def get(self, request):
        try:
            api_response = get_url_response(BASE_URL)
            response_data = exact_response_data(api_response)
            return Response(response_data)
        except Exception as e:
            return Response(f"ERROR:{e}")


@api_view(["POST"])
def register(request):
    """
    Register a new user and return their token.
    """
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(
            {"error": "Both username and password are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.save()

    token, created = Token.objects.get_or_create(user=user)

    return Response({"token": token.key}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def login(request):
    """
    Log in a user and return their token.
    """
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(
            {"error": "Both username and password are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = User.objects.filter(username=username).first()

    if user is None or not user.check_password(password):
        return Response(
            {"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED
        )

    token, created = Token.objects.get_or_create(user=user)

    return Response({"token": token.key}, status=status.HTTP_200_OK)
