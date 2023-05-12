from django.urls import path 
from . import views
from rest_framework.routers import SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router=SimpleRouter()
router.register('institution', views.InstitutionViewset)
router.register('institution/faculty', views.FacultyViewset)
router.register('institution/department', views.DepartmentViewset)

urlpatterns=[
    
]+router.urls