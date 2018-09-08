# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from temp_test.models import Type, Category, Variety, Condition, Grow, Dataset


admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Variety)
admin.site.register(Condition)
admin.site.register(Grow)
admin.site.register(Dataset)
