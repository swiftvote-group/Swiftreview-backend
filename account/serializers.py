from rest_framework import serializers
from .models import CustomUser, Profile


class StudentSignSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","email", 'profile_id',"username", "first_name","middle_name", "password"]
        extra_kwargs={"password":{"write_only":True},"id":{"read_only":True}}

        # def create(self, validate_data):
        #     print('Helooo')
        #     user=CustomUser(
        #         username=validate_data["username"],
        #         email=validate_data["email"],
        #         first_name=validate_data["first_name"],
        #         middle_name=validate_data["middle_name"],
        #         last_name=validate_data["last_name"],
        #         is_student=True
        #     )
        #     print(validate_data["password"],"h hq")
        #     user.set_password(validate_data["password"])
        #     user.save()
        #     return user

class StaffSignSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","email", 'profile_id',"username", "first_name","middle_name", "password"]
        extra_kwargs={"password":{"write_only":True},"id":{"read_only":True}}

        # def create(self, validate_data):
        #     user=CustomUser(
        #         username=validate_data["username"],
        #         email=validate_data["email"],
        #         first_name=validate_data["first_name"],
        #         middle_name=validate_data["middle_name"],
        #         last_name=validate_data["last_name"],
        #         is_sch_staff=True
        #     )
        #     user.set_password(validate_data["password"])
        #     user.save()
        #     return user
        
class ParentSignSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","email",'profile_id', "username", "first_name","middle_name", "password"]
        extra_kwargs={"password":{"write_only":True},"id":{"read_only":True}}

        # def create(self, validate_data):
        #     user=CustomUser(
        #         username=validate_data["username"],
        #         email=validate_data["email"],
        #         first_name=validate_data["first_name"],
        #         middle_name=validate_data["middle_name"],
        #         last_name=validate_data["last_name"],
        #         is_parent=True
        #     )
        #     user.set_password(validate_data["password"])
        #     user.save()
        #     return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=["id","user","institution","faculty","department","level",
            "file_proof", "phone_number","location" ,"birth_date","linkedln",
              "twitter","bio","profile_image" ]
        extra_kwargs={"file_proof":{"write_only":True},"id":{"read_only":True}}

class RequestPasswordTokenSerializer(serializers.Serializer):
	email=serializers.EmailField()

class NewPasswordSerializer(serializers.Serializer):
	new_password=serializers.CharField(max_length=100)

                                            