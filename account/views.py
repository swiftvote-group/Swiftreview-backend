from django.shortcuts import render
from .models import CustomUser, Profile
from .serializers import StaffSignSerializer, StudentSignSerializer, ParentSignSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class StudentAccountViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=StaffSignSerializer

    def get(self, *args, **kwargs):
        students=CustomUser.objects.filter(is_student=True)
        serializer=self.serializer_class(students, many=True)
        return Response({"details":serializer.data})
        
class StaffAccountViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=StudentSignSerializer

class ParentAccountViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=ParentSignSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["first_name"] = user.first_name
        token["middle_name"] = user.middle_name
        token["last_name"] = user.last_name
        token["email"] = user.email

        return token


class CustomTokenObtain(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer