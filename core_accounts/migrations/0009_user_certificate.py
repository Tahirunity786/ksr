# Generated by Django 5.0.6 on 2024-06-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0008_user_auth_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='certificate',
            field=models.FileField(db_index=True, default=None, null=True, upload_to='student/certificates'),
        ),
    ]
