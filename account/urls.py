from django.urls import path 
from . import views
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router=SimpleRouter()
router.register('student/account', views.StudentAccountViewset)
router.register('staff/account', views.StaffAccountViewset)
router.register('parent/account', views.ParentAccountViewset)
router.register('profile/account', views.UsersAcoountProfileViewset)

urlpatterns=[
    # JWT views
    path("token/", views.CustomTokenObtain.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    
    # Reset user password
    path("request-password-reset/", views.SendUserPasswordToken.as_view()),
	path("changepassword/<uidb64>/<token>/", views.ChangeUserPassword.as_view()),
]+router.urls