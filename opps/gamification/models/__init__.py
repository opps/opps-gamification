#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from opps.gamification.signals import generic_signal


try:
    OPPS_MODELS = [app for app in models.get_models()\
                   if 'opps.' in app.__module__]
except ImportError:
    OPPS_MODELS = []

for model in OPPS_MODELS:
    models.signals.post_save.connect(generic_signal, sender=model)
