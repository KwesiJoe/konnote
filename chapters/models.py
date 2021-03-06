# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from subjects.models import Subject
from django.contrib.auth.models import User
from levels.models import Level
from utility.helpers import generate_str


class Chapter(models.Model):
    subject = models.ForeignKey(Subject, default='', on_delete=models.CASCADE)
    level = models.ForeignKey(Level, default='', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    created_by = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.subject.name + ' | ' + self.level.name + ' | ' + self.name

    def __str__(self):
        return generate_str([self.subject.name, self.level.name, self.name])
