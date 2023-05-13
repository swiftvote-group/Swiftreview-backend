from django.urls import path 
from . import views
from rest_framework.routers import SimpleRouter


router=SimpleRouter()
router.register('institution/profile', views.InstitutionProfileViewset)
router.register('institution/review', views.InstitutionReviewViewset)

urlpatterns=[
    
]+router.urls