# Generated by Django 5.0.6 on 2024-06-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0011_rename_subjects_user_subject_remove_user_certificate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile/images'),
        ),
    ]
