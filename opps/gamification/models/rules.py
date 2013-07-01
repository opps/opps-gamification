#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from opps.core.models import Publishable, Slugged
from opps.boxes.models import OPPS_APPS


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
    badge = models.ForeignKey('gamification.Badge')
    score = models.ForeignKey('gamification.Score')

    class Meta:
        verbose_name = _("Rule")
        verbose_name_plural = _("Rules")
