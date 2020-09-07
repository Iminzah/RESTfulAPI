# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from .models import Employees
from serializer import EmployeesSerializer

class EmployeesList(APIView):

     def get(self):
         employee1=Employees.objects.all()
         serializer=EmployeesSerializer(employee1,many=True)
         return Response(serializer.data)
     
     def post(self):
         pass   


