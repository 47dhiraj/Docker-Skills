# yo talako line of codes will allow django to find celery tasks automatically

from .celery import app as celery_app

__all__ = ("celery_app",)