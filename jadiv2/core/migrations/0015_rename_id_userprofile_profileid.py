# Generated by Django 4.2.11 on 2024-05-28 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_userprofile_customuserinterest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='id',
            new_name='profileId',
        ),
    ]