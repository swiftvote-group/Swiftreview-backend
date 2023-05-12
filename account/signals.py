from .models import CustomUser, Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a profile for each new user"""
    if created:
        Profile.objects.create(user=instance)
        
        