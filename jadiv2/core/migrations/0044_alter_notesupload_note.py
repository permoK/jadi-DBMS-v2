# Generated by Django 4.2.9 on 2024-06-11 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_notesupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesupload',
            name='note',
            field=models.FileField(upload_to='../core/static/assets/'),
        ),
    ]
