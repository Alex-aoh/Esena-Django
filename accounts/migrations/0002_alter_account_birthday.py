# Generated by Django 4.2.4 on 2023-08-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Birthday'),
        ),
    ]
