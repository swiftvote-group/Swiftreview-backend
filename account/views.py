from django.shortcuts import render
from .models import CustomUser, Profile, ResetToken
from .serializers import StaffSignSerializer, StudentSignSerializer, ParentSignSerializer,ProfileSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions

# Password change view imports
from rest_framework import views
# from .serializers import PasswordResetSerializer
from .serializers import RequestPasswordTokenSerializer, NewPasswordSerializer
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site  
from .tokens import account_activation_token   
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from django.http import Http404
from .models import ResetToken
from datetime import timedelta
from datetime import datetime, timedelta
from django.utils import timezone

User = get_user_model()
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

class SendUserPasswordToken(generics.GenericAPIView):
	# serializer_class=RequestPasswordTokenSerializer

	def post(self, request, *args, **kwargs):
		email=request.data['email']
		try:
			user=CustomUser.objects.get(email=email)
		except:
			return Response({"error":"User with this email does not exist !"},status=status.HTTP_404_NOT_FOUND)
		if user.is_active:
			uid=urlsafe_base64_encode(force_bytes(user.pk))
			token=account_activation_token.make_token(user)
			ResetToken.objects.filter(user=user).delete() #Get users previous token and delete
			ResetToken.objects.create(user=user, token=token)
			subject="Passoword Reset Email"
			html_content = render_to_string('changepassword.html', {'name': user.first_name})
			msg= EmailMultiAlternatives(subject, 'password@swiftreview.com',[email])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			return Response({"success":"Reset link sent check your mail","token":token, "uuid":uid})
			
		else:
			return Response({"error":"Your account is not activated yet so you cannot change your poassword"},status=status.HTTP_403_FORBIDDEN)

class ChangeUserPassword(generics.CreateAPIView):
	
	def post(self,request, *args, **kwargs):
		uidb64=request.data["uidb64"]
		token=request.data["token"]
		new_password= request.data["new_password"]

		try:
			uid=force_str(urlsafe_base64_decode(uidb64))
			user=CustomUser.objects.get(pk=uid)
		except(TypeError, ValueError, OverflowError):
			user=None
		if user is not None and account_activation_token.check_token(user, token):
			user.set_password(new_password)
			user.save()
            # Delete the user's token
			ResetToken.objects.filter(user=user).delete()
			return Response({"success":"Passowrd change successfully"})
		return Response({"error":"Unable to chnage password due to incorrect token"},status=status.HTTP_403_FORBIDDEN)	