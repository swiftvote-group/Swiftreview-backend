from  django.utils.text import slugify
from django.db import models

# Create your models here.

class Institution(models.Model):
    school_name=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.school_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.school_name +"_"+ str(self.id))
        return super(Institution,self).save(*args, **kwargs)

class Faculty(models.Model):
    institution=models.ForeignKey(Institution,  on_delete=models.CASCADE)
    name_of_faculty=models.CharField(max_length=20)

    def __str__(self):
        return self.name_of_faculty

class Department(models.Model):
    faculty=models.ForeignKey(Faculty,  on_delete=models.CASCADE)
    name_of_dept=models.CharField(max_length=20)

    def __str__(self):
        return self.name_of_dept