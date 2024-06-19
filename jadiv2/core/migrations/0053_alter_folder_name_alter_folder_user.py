# Generated by Django 4.2.9 on 2024-06-18 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_alter_folder_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='folder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
    ]