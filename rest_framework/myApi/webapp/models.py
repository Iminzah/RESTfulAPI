# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Employees(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    id_number=models.IntegerField()
    phone_number=models.IntegerField()


    def __str__(self):
        return self.first_name
    