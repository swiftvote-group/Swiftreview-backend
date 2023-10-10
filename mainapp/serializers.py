from rest_framework import serializers
from .models import InstitutionProfile, Review


class InstitutionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstitutionProfile
        fields=["id","staff","institution","category","sub_category","logo","no_of_campuses","no_of_faculties", "no_of_departments",
                "population", "acceptance_rate","graduation_rate","cost_range", "file_proof", "email","linkedln", 
                "twitter", "website", "address","phone","date_founded",]
        extra_kwargs={"id":{"read_only":True}}

class InstitutionRewiewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=[
            "id","title","slug","poster","institution","review_type","photo","date_of_expierence",
            "use_photo_review","content","review_image","star_rate","learning_rate","safety_support_rate",
            "likehood_to_recommend_rate","verification_status","anonymous","vote_count","date_posted"
        ]
        extra_kwargs={"id":{"read_only":True}, "slug":{"read_only":True}}

class MVPRewiewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=[
            "id","title","poster","institution","review_type","photo","date_of_expierence",
            "use_photo_review","content","review_image","star_rate",
            "anonymous","date_posted",'poster_name',
            'institution_name',
        ]
        extra_kwargs={"id":{"read_only":True}}