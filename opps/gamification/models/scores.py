#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from opps.core.models import NotUserPublishable


class Score(NotUserPublishable):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    score = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("Score")
        verbose_name_plural = _("Scores")
