# Generated by Django 5.0.6 on 2024-06-09 09:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_id', models.CharField(db_index=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True, db_index=True)),
                ('price', models.IntegerField(db_index=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipt_made_by', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_made_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
