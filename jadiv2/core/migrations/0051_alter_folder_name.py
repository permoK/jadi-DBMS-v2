# Generated by Django 4.2.9 on 2024-06-18 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_alter_foldername_user_alter_foldername_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.foldername'),
        ),
    ]
