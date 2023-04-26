from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student


class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SingleStudentView(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
