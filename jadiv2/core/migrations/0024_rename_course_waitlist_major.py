# Generated by Django 4.2.11 on 2024-06-03 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_waitlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waitlist',
            old_name='course',
            new_name='major',
        ),
    ]
