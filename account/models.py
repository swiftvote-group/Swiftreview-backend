import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from relatedapp.models import Institution, Department, Faculty


class UserManager(BaseUserManager):
    """Manager for User Profile"""

    def create_user(
        self,
        username,
        first_name,
        middle_name,
        last_name,
        email,
        password=None,
    ):
        """Create a new user"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        username,
        first_name,
        middle_name,
        last_name,
        email,
        password=None,
    ):
        """Create a new superuser"""
        user = self.create_user(
            username, first_name, middle_name, last_name, email, password
        )
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Databse model for users in the system"""

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    date_joined=models.DateField(auto_now=True)

    is_parent=models.BooleanField(default=False)
    is_sch_staff=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "middle_name",
        "last_name",
    ]

    def __str__(self):
        return self.email
    

class Profile(models.Model):
    """Database model for user profiles"""

    levels=[
        ("100", "100"),
        ("200", "200"),
        ("300", "300"),
        ("400", "400"),
        ("500", "500"),
        ("600", "600"),
        ("PG", "PG"),
        ("Masters", "Masters"),
        ("PhD", "PhD"),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    institution=models.ForeignKey(Institution,  on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,  on_delete=models.CASCADE)
    department=models.ForeignKey(Department,  on_delete=models.CASCADE)
    level=models.CharField(max_length=200, choices=levels)
    file_proof=models.FileField(upload_to='Users_file_proofs/', blank=True)
    phone_number=models.CharField(max_length=15)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    linkedln=models.URLField(blank=True)
    twitter=models.URLField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    def __str__(self):
        """Return string representation of the user's profile"""
        return self.user.username + "'s Profile"
    

