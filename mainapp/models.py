from django.db import models
from account.models import CustomUser
from relatedapp.models import Institution, Department, Faculty
from  django.utils.text import slugify

    
class InstitutionProfile(models.Model):

    Categories=[
        ("University", "University"),
        ("Polytechnic", "Polytechnic"),
        ("Colledge_of_Education", "Colledge_of_Education"),
      
    ]
    Sub_Categories=[
        ("Federal", "Federal"),
        ("State", "State"),
        ("Private", "Private"),
        ("Non-Profit", "Non-Profit"),
      
    ]

    Features =[
        ("Remote-Learning", "Remote-Learning"),
        (" All-Inclusive","All-Inclusive"),
        ("All-Exclusive","All-Exclusive")
    ]
    staff=models.ManyToManyField(CustomUser)
    institution=models.OneToOneField(Institution,  on_delete=models.CASCADE)
    category=models.CharField(max_length=30, choices=Categories,null=True,)
    sub_category=models.CharField(max_length=30, choices=Sub_Categories,null=True,) 
    logo= models.ImageField(upload_to="institution_logo", null=True, blank=True)
    no_of_campuses=models.IntegerField(null=True,)
    no_of_faculties=models.IntegerField(null=True,)
    no_of_departments=models.IntegerField(null=True,)
    population=models.IntegerField(null=True,)
    acceptance_rate=models.CharField(max_length=10,null=True,)
    graduation_rate=models.CharField(max_length=10,null=True,)
    cost_range=models.CharField(max_length=30)
    file_proof=models.FileField(upload_to='School_file_proofs/', blank=True,null=True,)
    email=models.EmailField(unique=True,null=True,)
    linkedln=models.URLField(blank=True,null=True,)
    twitter=models.URLField(blank=True,null=True,)
    website=models.URLField(blank=True,null=True,)
    address=models.CharField(max_length=50,null=True,)
    phone=models.CharField(max_length=20,null=True,)
    date_founded=models.DateField(null=True,)


    def __str__(self):
        return f"{self.institution.school_name}'s profile"


class Review(models.Model):

    Review_Types=[
        ("Content_Review", "Content_Review"),
        ("Phote_Review", "Phote_Review")
    ]
    title=models.CharField(max_length=50,null=True, blank=True)
    slug=models.SlugField(unique=True,null=True, blank=True, help_text="This will be auto generated. leave blank")
    poster=models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)
    institution=models.ForeignKey(Institution,  on_delete=models.CASCADE,null=True, blank=True)
    review_type=models.CharField(max_length=20, choices=Review_Types,null=True, blank=True)
    photo= models.ImageField(upload_to="photo_reviews", null=True, blank=True)
    date_of_expierence=models.DateField()
    use_photo_review=models.BooleanField()
    content=models.CharField(max_length=500, blank=True, null=True)
    review_image=models.ImageField(upload_to="review_photo", blank=True, null=True)
    star_rate=models.FloatField(null=True, blank=True)
    learning_rate=models.FloatField(null=True, blank=True)
    safety_support_rate=models.FloatField(null=True, blank=True)
    likehood_to_recommend_rate=models.FloatField(null=True, blank=True)
    verification_status=models.BooleanField(default=False,null=True, blank=True)
    anonymous=models.BooleanField(default=False,null=True, blank=True)
    vote_count=models.IntegerField(default=0,null=True, blank=True)
    date_posted=models.DateField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return f"{self.institution}'s Review | Posted {self.date_posted}"
    @property
    def poster_name(self):
        return f"{self.poster.first_name} {self.poster.last_name}"
    @property
    def institution_name(self):
        return self.institution.school_name
    # def save(self, *args, **kwargs):
    #     self.slug= slugify(self.title + str(self.id))
    #     return super(Review,self).save(*args, **kwargs)