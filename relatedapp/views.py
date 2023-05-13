from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import InstitutionSerializer, FacultySerializer, DepartmentSerializer
from .models import  Institution, Faculty, Department
from rest_framework import permissions
# Create your views here.


class InstitutionViewset(viewsets.ModelViewSet):
    queryset=Institution.objects.all()
    serializer_class=InstitutionSerializer
    permission_classes=[permissions.IsAuthenticated]
    

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        try:
            print("Hello")
            self.perform_create(serializer)
        except:
            return Response({"details":"Institution with this name already exist"}, status=status.HTTP_400_BAD_REQUEST) 
        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

class FacultyViewset(viewsets.ModelViewSet):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializer
    permission_classes=[permissions.IsAuthenticated]

class DepartmentViewset(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    permission_classes=[permissions.IsAuthenticated]