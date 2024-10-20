"""
Module: user apps

This module defines the configuration class for the user app.
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserConfig(AppConfig):
    """Configuration class for the user app."""

    name = "user"
    verbose_name = _("User")
