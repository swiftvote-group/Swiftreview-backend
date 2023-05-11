# Generated by Django 4.2.1 on 2023-05-11 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('relatedapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='This will be auto generated. leave blank', unique=True)),
                ('logo', models.ImageField(upload_to='institution_logo')),
                ('review_type', models.CharField(choices=[('Content_Review', 'Content_Review'), ('Phote_Review', 'Phote_Review')], max_length=20)),
                ('date_of_expierence', models.DateField()),
                ('use_photo_review', models.BooleanField()),
                ('content', models.CharField(blank=True, max_length=500, null=True)),
                ('review_image', models.ImageField(blank=True, null=True, upload_to='review_photo')),
                ('star_rate', models.FloatField()),
                ('learning_rate', models.FloatField()),
                ('safety_support_rate', models.FloatField()),
                ('likehood_to_recommend_rate', models.FloatField()),
                ('verification_status', models.BooleanField(default=False)),
                ('anonymous', models.BooleanField(default=False)),
                ('vote_count', models.IntegerField(default=0)),
                ('date_posted', models.DateField(auto_now=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatedapp.institution')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('University', 'University'), ('Polytechnic', 'Polytechnic'), ('Colledge_of_Education', 'Colledge_of_Education')], max_length=30)),
                ('sub_category', models.CharField(choices=[('Federal', 'Federal'), ('State', 'State'), ('Private', 'Private'), ('Non-Profit', 'Non-Profit')], max_length=30)),
                ('no_of_campuses', models.IntegerField()),
                ('no_of_faculties', models.IntegerField()),
                ('no_of_departments', models.IntegerField()),
                ('population', models.IntegerField()),
                ('acceptance_rate', models.CharField(max_length=10)),
                ('graduation_rate', models.CharField(max_length=10)),
                ('cost_range', models.CharField(max_length=30)),
                ('file_proof', models.FileField(blank=True, upload_to='School_file_proofs/')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('linkedln', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('date_founded', models.DateField()),
                ('institution', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='relatedapp.institution')),
                ('staff', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
