from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import InstitutionSerializer, FacultySerializer, DepartmentSerializer,NewsletterSerializer
from .models import  Institution, Faculty, Department, Newsletter
from rest_framework import permissions
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
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


# Allow users subscribe to newsletter

class NewletterView(generics.GenericAPIView):
    serializer_class=NewsletterSerializer
    def post(self, request, *args, **kwargs):

        email=request.data["email"]
        print(email, "test")
        Newsletter.objects.all().delete()
        try:
            Newsletter.objects.create(email=email)
        except:
            return Response({"detail":"Already a subscriber !!"}, status=status.HTTP_400_BAD_REQUEST)
        subject="Welcome to SEGNAU newsletter"
        # Render the HTML template using the user's email and name
        html_content = render_to_string('newletter_subscibe.html', {'email': email})

        # Create the EmailMultiAlternatives object
        email_message = EmailMultiAlternatives(subject=subject,
            from_email="nwaforglory6@gmail.com",
            to=[email],
        )
        # Attach the HTML content to the email message
        email_message.attach_alternative(html_content, "text/html")
        # Send the email
        email_message.send()
        return Response({"detail":"Thank you for subscribing."}, status=status.HTTP_200_OK)

class SubscribersList(generics.ListAPIView):
    queryset=Newsletter.objects.all()
    serializer_class=NewsletterSerializer

    # Get list of all subscribers
    def get(self, request, *args, **kwargs):
        serializer=self.serializer_class(self.get_queryset(), many=True)
        return Response({"details":serializer.data},status=status.HTTP_200_OK)