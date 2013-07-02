#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from .models.rules import Rule


admin.site.register(Rule)
