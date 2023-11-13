# -*- coding: utf-8 -*-
import os

from django.conf import settings
from django.test import TestCase
from unittest import mock
from unittest.mock import MagicMock, PropertyMock
from django_live_log.views import log_streamer, dll

#from django_live_log.url import urlpatterns as dll_urlpatterns
# url(r'^dll/', include('django_live_log.urls')),

class TestLogStreamer(TestCase):
    def test_ok(self):
        # Just test module can be imported
        pass
