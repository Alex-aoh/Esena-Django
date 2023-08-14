# Generated by Django 4.2.4 on 2023-08-06 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth0ManagementApiToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=10000, verbose_name='Token')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Auth0User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth0_id', models.CharField(max_length=255, unique=True, verbose_name='Auth0 ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Auth0 Email')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Auth0 Email Verified')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth0user', to=settings.AUTH_USER_MODEL, verbose_name='Django User')),
            ],
        ),
    ]