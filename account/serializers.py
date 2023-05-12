from rest_framework import serializers
from .models import CustomUser


class StudentSignSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","email", "username", "first_name","middle_name", "password"]
        extra_kwargs={"password":{"write_only":True},"id":{"read_only":True}}

        def create(self, validate_data):
            user=CustomUser(
                username=validate_data["username"],
                email=validate_data["email"],
                first_name=validate_data["first_name"],
                middle_name=validate_data["middle_name"],
                last_name=validate_data["last_name"],
                is_student=True
            )
            user.set_password(validate_data["password"])
            user.save()
            return user

class StaffSignSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","email", "username", "first_name","middle_name", "password"]
        extra_kwargs={"password":{"write_only":True},"id":{"read_only":True}}

        def create(self, validate_data):
            user=CustomUser(
                username=validate_data["username"],
                email=validate_data["email"],
                first_name=validate_data["first_name"],
                middle_name=validate_data["middle_name"],
                last_name=validate_data["last_name"],
                is_sch_staff=True
            )
            user.set_password(validate_data["password"])
            user.save()
            return user
        
class ParentSignSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","email", "username", "first_name","middle_name", "password"]
        extra_kwargs={"password":{"write_only":True},"id":{"read_only":True}}

        def create(self, validate_data):
            user=CustomUser(
                username=validate_data["username"],
                email=validate_data["email"],
                first_name=validate_data["first_name"],
                middle_name=validate_data["middle_name"],
                last_name=validate_data["last_name"],
                is_parent=True
            )
            user.set_password(validate_data["password"])
            user.save()
            return user

                                            