# Generated by Django 4.2.9 on 2024-06-18 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_foldername_alter_folder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foldername',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
        migrations.AlterModelTable(
            name='foldername',
            table='folder_names',
        ),
    ]