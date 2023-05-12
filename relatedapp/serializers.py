from rest_framework import serializers
from account.models import CustomUser
from .models import Institution, Faculty, Department


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institution
        fields=["school_name"]

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=["institution", "name_of_faculty"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=["faculty", "name_of_dept"]