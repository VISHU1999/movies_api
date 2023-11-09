from django.urls import include, path

from movie_app import views

urlpatterns = [
    path("movies/", views.ActorViewSet.as_view(), name="movie-list"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
]
