# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Food(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('name',)


class Restaurant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    foods = models.ManyToManyField(Food)

    class Meta:
        ordering = ('name',)

# Create your models here.
