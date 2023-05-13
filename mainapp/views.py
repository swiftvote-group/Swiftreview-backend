from django.shortcuts import render
from .serializers import InstitutionRewiewSerializer, InstitutionProfileSerializer
from .models import Review, InstitutionProfile
from rest_framework import viewsets

# Create your views here.

class InstitutionProfileViewset(viewsets.ModelViewSet):
    queryset=InstitutionProfile.objects.all()
    serializer_class=InstitutionProfileSerializer

class InstitutionReviewViewset(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=InstitutionRewiewSerializer