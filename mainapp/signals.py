from relatedapp.models import Institution
from .models import InstitutionProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Institution)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a profile for each new user"""
    if created:
        InstitutionProfile.objects.create(institution=instance)
        
        