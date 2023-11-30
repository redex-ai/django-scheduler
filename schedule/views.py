import datetime
from urllib.parse import quote

import dateutil.parser
import pytz
from django.conf import settings
from django.db.models import F, Q
from django.http import (
    Http404,
    HttpResponseBadRequest,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone

try:
    from django.utils.http import url_has_allowed_host_and_scheme
except ImportError:
    # Django<=2.2
    from django.utils.http import is_safe_url as url_has_allowed_host_and_scheme

import logging

logger = logging.getLogger(__name__)

# Existing code...
