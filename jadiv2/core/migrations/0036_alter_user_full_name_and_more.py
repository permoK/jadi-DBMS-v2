# Generated by Django 4.2.9 on 2024-06-10 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_usereducationdetails_fx_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='usereducationdetails',
            name='fx_full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user', to_field='full_name'),
        ),
    ]
