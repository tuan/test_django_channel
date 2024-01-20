import logging
import os

from django.apps import AppConfig

from project import settings

logger = logging.getLogger(__name__)


class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

    def ready(self):
        logger.info(
            f"DEBUG={settings.DEBUG},"
            f"\nEMAIL_BACKEND_TYPE={os.getenv('EMAIL_BACKEND_TYPE')}"
        )
