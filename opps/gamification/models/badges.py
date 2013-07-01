#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from opps.core.models import Publishable, Slugged


class Badge(Publishable, Slugged):
    name = models.CharField(_(u"Name"), max_length=140, db_index=True)

    class Meta:
        verbose_name = _("Badge")
        verbose_name_plural = _("Badges")


class BadgeAchievement(Publishable):
    score = models.IntegerField(default=0)
    badge = models.ForeignKey('gamification.Badge')

    class Meta:
        verbose_name = _("Badge Achievement")
        verbose_name_plural = _("Badges Achievement")
