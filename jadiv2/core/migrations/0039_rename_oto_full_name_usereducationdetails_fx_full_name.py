# Generated by Django 4.2.9 on 2024-06-10 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_rename_fx_full_name_usereducationdetails_oto_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usereducationdetails',
            old_name='oto_full_name',
            new_name='fx_full_name',
        ),
    ]
