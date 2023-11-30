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
logging.basicConfig(level=logging.DEBUG)


class EventListManager:
    def __init__(self, events):
        self.events = events

    def occurrences_after(self, after=None):
        logger.debug('Calling occurrences_after function')
        ...
        logger.debug('Exiting occurrences_after function')


# Rest of the code...
