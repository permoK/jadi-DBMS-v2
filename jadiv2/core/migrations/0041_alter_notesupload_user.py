# Generated by Django 4.2.9 on 2024-06-11 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_rename_fx_full_name_usereducationdetails_oto_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesupload',
            name='user',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
