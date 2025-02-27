# Generated by Django 5.1.6 on 2025-02-11 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_citizen_password_alter_institute_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='institute',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
