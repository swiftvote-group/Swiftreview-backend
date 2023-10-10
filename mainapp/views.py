from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import InstitutionRewiewSerializer, MVPRewiewSerializer,InstitutionProfileSerializer
from .models import Review, InstitutionProfile
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import GenericAPIView

# Create your views here.

class InstitutionProfileViewset(viewsets.ModelViewSet):
    queryset=InstitutionProfile.objects.all()
    serializer_class=InstitutionProfileSerializer
    # permission_classes=[permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            # Apply custom permission classes for update and delete actions
            permission_classes = [permissions.IsAuthenticated]
        else:
            # Use default permissions for other actions
            permission_classes = [permissions.AllowAny]

        return [permission() for permission in permission_classes]

class InstitutionReviewViewset(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=InstitutionRewiewSerializer
    # permission_classes=[permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            # Apply custom permission classes for update and delete actions
            permission_classes = [permissions.IsAuthenticated]
        else:
            # Use default permissions for other actions
            permission_classes = [permissions.AllowAny]

        return [permission() for permission in permission_classes]

class MVPRewiew(GenericAPIView):
    queryset=Review.objects.all()
    serializer_class=MVPRewiewSerializer
    # permission_classes=[permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            # Apply custom permission classes for update and delete actions
            permission_classes = [permissions.IsAuthenticated]
        else:
            # Use default permissions for other actions
            permission_classes = [permissions.AllowAny]

        return [permission() for permission in permission_classes]

    def get(self, request):
        reviews=Review.objects.all()
        serializer=serializer_class(reviews, many=True)
        return Response(serializer)

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            instance=serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


