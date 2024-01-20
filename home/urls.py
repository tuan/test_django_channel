from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.urls import path
from django.views.decorators.cache import cache_page

from project import settings

from .views import HomeView

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)
urlpatterns = [
    path("", cache_page(CACHE_TTL)(HomeView.as_view()), name="home"),
]
