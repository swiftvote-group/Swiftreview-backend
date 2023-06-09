# Generated by Django 4.2.1 on 2023-05-11 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('relatedapp', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('middle_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('date_joined', models.DateField(auto_now=True)),
                ('is_parent', models.BooleanField(default=False)),
                ('is_sch_staff', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500'), ('600', '600'), ('PG', 'PG'), ('Masters', 'Masters'), ('PhD', 'PhD')], max_length=200)),
                ('file_proof', models.FileField(blank=True, upload_to='Users_file_proofs/')),
                ('phone_number', models.CharField(max_length=15)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('linkedln', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_images/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatedapp.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatedapp.faculty')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatedapp.institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
