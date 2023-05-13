from django.urls import path 
from . import views
from rest_framework.routers import SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router=SimpleRouter()
router.register('student/account', views.StudentAccountViewset)
router.register('staff/account', views.StaffAccountViewset)
router.register('parent/account', views.ParentAccountViewset)
router.register('profile/account', views.UsersAcoountProfileViewset)
schema_view = get_schema_view(
   openapi.Info(
      title="swiftreview Backend API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns=[
    # JWT views
    path("token/", views.CustomTokenObtain.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+router.urls