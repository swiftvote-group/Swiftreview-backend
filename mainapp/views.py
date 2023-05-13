from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import InstitutionRewiewSerializer, InstitutionProfileSerializer
from .models import Review, InstitutionProfile
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

class InstitutionProfileViewset(viewsets.ModelViewSet):
    queryset=InstitutionProfile.objects.all()
    serializer_class=InstitutionProfileSerializer
    permission_classes=[permissions.IsAuthenticated]

class InstitutionReviewViewset(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=InstitutionRewiewSerializer
    permission_classes=[permissions.IsAuthenticated]


