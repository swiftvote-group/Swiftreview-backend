from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InstitutionSerializer, FacultySerializer, DepartmentSerializer
from .models import  Institution, Faculty, Department
# Create your views here.


class InstitutionViewset(viewsets.ModelViewSet):
    queryset=Institution.objects.all()
    serializer_class=InstitutionSerializer

class FacultyViewset(viewsets.ModelViewSet):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializer

class DepartmentViewset(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer