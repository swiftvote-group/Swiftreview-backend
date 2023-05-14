from django.shortcuts import render
from .models import CustomUser, Profile
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


# view for the password change
class SendUserPasswordToken(generics.CreateAPIView):
    serializer_class = RequestPasswordTokenSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email, is_active=True)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        # Create user's token
        expiration_date = datetime.now() + timedelta(minutes=5) 
        ResetToken.objects.create(user=user, token=token, expiration_date=expiration_date)

        # subject = 'Password Reset'
        # message = f'Hi {user.username}, click on this link to reset your password: {uid}/{token}'
        # from_email = 'noreply@agro360.com'
        # recipient_list = [email]

        # send_mail(subject, message, from_email, recipient_list)

        return Response({'success': 'Password reset link sent. Please check your email. Link expires in 5mins'}, status=status.HTTP_200_OK)

class ChangeUserPassword(generics.GenericAPIView):
    serializer_class=NewPasswordSerializer
        
    def get_object(self, uidb64):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            return User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise Http404

    def post(self, request, *args, **kwargs):
        uidb64 = self.kwargs["uidb64"]
        token = self.kwargs["token"]
        new_password = request.data["new_password"]
        user = self.get_object(uidb64)
        print(user, "users")
        try:
            reset_token=ResetToken.objects.get(user=user)
        except:
            return Response({"details":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        if account_activation_token.check_token(user, token):
            if timezone.now() <= reset_token.expiration_date:
                print(timezone.now())
                print(reset_token.expiration_date)
                user.set_password(new_password)
                user.save()
                reset_token.delete()
                return Response({"success": "Password changed successfully."})
            return Response({"details": "Token Expired"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Unable to change password due to incorrect token."}, status=status.HTTP_400_BAD_REQUEST)