from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .mock import Mock_API
from .utils import exact_response_data, get_url_response

User = get_user_model()


# Create your tests here.
class MovieAPITestCase(TestCase):
    """
    Test case for the Actor API.

    This test case includes tests for both authenticated and unauthenticated users
    accessing the movies list API, as well as testing the correctness of API functions.

    Attributes:
        user: A test user for authentication in the test cases.
    """

    def setUp(self):
        """Creates a test user with a username and password."""
        self.user = User.objects.create(username="testuser", password="testpassword")

    def test_unauthenticated_user_can_access_actor_api(self):
        """Test that an unauthenticated user cannot access the movies API."""
        url = reverse("movie-list")
        # Make a GET request to the API
        client = APIClient()
        response = client.get("/movies", follow=True)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @patch("movie_app.views.get_url_response")
    def test_authenticated_user_can_access_actor_api(self, mock_get_url_response):
        """Test that an authenticated user can access the movies API"""
        mock_get_url_response.return_value = Mock_API
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get("/movies", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_works_and_functions_are_correct(self):
        """Test the correctness of the utils functions."""

        response_data = exact_response_data(Mock_API)

        self.assertIsNotNone(response_data)
        self.assertIsInstance(response_data, list)
        self.assertTrue(all(isinstance(item, dict) for item in response_data))
