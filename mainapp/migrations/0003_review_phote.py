# Generated by Django 4.2.1 on 2023-05-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_review_logo_institutionprofile_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='phote',
            field=models.ImageField(blank=True, null=True, upload_to='photo_reviews'),
        ),
    ]