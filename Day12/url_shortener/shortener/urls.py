from django.urls import path

from .views import (
    ShortenURLView,
    ShortURLDetailView,
    ShortURLStatsView,
    RedirectURLView,
)

urlpatterns = [
    path(
        "shorten",
        ShortenURLView.as_view(),
        name="create-short-url",
    ),
    path(
        "shorten/<str:short_code>",
        ShortURLDetailView.as_view(),
        name="short-url-detail",
    ),
    path(
        "shorten/<str:short_code>/stats",
        ShortURLStatsView.as_view(),
        name="short-url-stats",
    ),
    path("<str:short_code>", RedirectURLView.as_view()),
]
