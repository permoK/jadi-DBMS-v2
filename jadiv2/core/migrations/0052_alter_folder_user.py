# Generated by Django 4.2.9 on 2024-06-18 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_alter_folder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foldername', to='core.foldername'),
        ),
    ]
