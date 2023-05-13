from django.shortcuts import render
from .models import CustomUser, Profile
from .serializers import StaffSignSerializer, StudentSignSerializer, ParentSignSerializer,ProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
# Create your views here.

class StudentAccountViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=StaffSignSerializer
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def list(self,request, *args, **kwargs):
        print("In the studentlist")
        students=CustomUser.objects.filter(is_student=True)
        serializer=self.serializer_class(students, many=True)
        return Response({"details":serializer.data}, status=status.HTTP_200_OK)

        
class StaffAccountViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=StudentSignSerializer

    def list(self,request, *args, **kwargs):
        print("In the stafflist")
        staffs=CustomUser.objects.filter(is_staff=True)
        serializer=self.serializer_class(staffs, many=True)
        return Response({"details":serializer.data}, status=status.HTTP_200_OK)

class ParentAccountViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=ParentSignSerializer

    def list(self,request, *args, **kwargs):
        print("In the parentslist")
        parents=CustomUser.objects.filter(is_parent=True)
        serializer=self.serializer_class(parents, many=True)
        return Response({"details":serializer.data}, status=status.HTTP_200_OK)

class UsersAcoountProfileViewset(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]

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