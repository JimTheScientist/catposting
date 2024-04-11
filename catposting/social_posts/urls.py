from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("oauth", views.oauth, name="oauth"),
    path("post", views.post, name="post"),
    path("post_submit", views.post_submit, name="post_submit")
]
