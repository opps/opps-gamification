#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .signals import generic_signal

from opps.core.models import Publishable, Slugged, NotUserPublishable
from opps.archives.models import get_file_path
from opps.boxes.models import OPPS_APPS


class Score(NotUserPublishable):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    score = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("Score")
        verbose_name_plural = _("Scores")


class Rule(Publishable, Slugged):
    name = models.CharField(_(u"Name"), max_length=140, db_index=True)
    application = models.CharField(_(u'Application'), max_length=150,
                                   choices=OPPS_APPS)
    action = models.CharField(_(u"Action"), max_length=140,
                              choices=(
                                  ('pre_save', _(u'Pre save')),
                                  ('pos_save', _(u'Pos save')),
                                  ('pre_delete', _(u'Pre delete')),
                                  ('pos_delete', _(u'Pos delete'))),
                              db_index=True)
    badge = models.ForeignKey(
        'gamification.Badge',
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_badge")
    score = models.ForeignKey(
        'gamification.Score',
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_score")

    class Meta:
        verbose_name = _("Rule")
        verbose_name_plural = _("Rules")


class Badge(Publishable, Slugged):
    name = models.CharField(_(u"Name"), max_length=140, db_index=True)
    archive = models.FileField(upload_to=get_file_path, max_length=255)

    class Meta:
        verbose_name = _("Badge")
        verbose_name_plural = _("Badges")


class BadgeAchievement(Publishable):
    score = models.IntegerField(default=0)
    badge = models.ForeignKey('gamification.Badge')

    class Meta:
        verbose_name = _("Badge Achievement")
        verbose_name_plural = _("Badges Achievement")


try:
    OPPS_MODELS = [app for app in models.get_models()\
                   if 'opps.' in app.__module__]
except ImportError:
    OPPS_MODELS = []

for model in OPPS_MODELS:
    models.signals.post_save.connect(generic_signal, sender=model)
