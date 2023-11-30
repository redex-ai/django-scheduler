import heapq
from functools import wraps

import logging

from django.conf import settings
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.utils import timezone

from schedule.settings import (
    CALENDAR_VIEW_PERM,
    CHECK_CALENDAR_PERM_FUNC,
    CHECK_EVENT_PERM_FUNC,
    CHECK_OCCURRENCE_PERM_FUNC,
)


logger = logging.getLogger(__name__)


class EventListManager:
    ...


def get_kwarg_or_param(request, kwargs, key):
    logger.debug(f'Getting value for key: {key}')
    value = None
    try:
        value = kwargs[key]
    except KeyError:
        if request.method == "GET":
            value = request.GET.get(key)
        elif request.method == "POST":
            value = request.POST.get(key)
    logger.debug(f'Value for key {key}: {value}')
    return value


# Rest of the code...
