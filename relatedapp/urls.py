from django.urls import path 
from . import views
from rest_framework.routers import SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router=SimpleRouter()
router.register('institution', views.InstitutionViewset)
router.register('faculty', views.FacultyViewset)
router.register('department', views.DepartmentViewset)

urlpatterns=[
    path('subscribe/', views.NewletterView.as_view()),
    path("subscriber_list/", views.SubscribersList.as_view()),
]+router.urls