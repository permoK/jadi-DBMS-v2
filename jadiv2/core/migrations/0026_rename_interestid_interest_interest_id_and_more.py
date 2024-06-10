# Generated by Django 4.2.11 on 2024-06-03 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_user_interests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interest',
            old_name='interestId',
            new_name='interest_id',
        ),
        migrations.RenameField(
            model_name='interest',
            old_name='interestName',
            new_name='interest_name',
        ),
        migrations.RenameField(
            model_name='learninginstitution',
            old_name='institutionId',
            new_name='institution_id',
        ),
        migrations.RenameField(
            model_name='learninginstitution',
            old_name='institutionName',
            new_name='institution_name',
        ),
        migrations.RenameField(
            model_name='usereducationdetails',
            old_name='learning_institution',
            new_name='fx_learning_institution',
        ),
        migrations.RenameField(
            model_name='usereducationdetails',
            old_name='student_major',
            new_name='fx_student_major',
        ),
        migrations.RenameField(
            model_name='waitlist',
            old_name='major',
            new_name='fx_major',
        ),
        migrations.RenameField(
            model_name='waitlist',
            old_name='name',
            new_name='fx_name',
        ),
        migrations.AlterModelTable(
            name='learninginstitution',
            table='learning_institution',
        ),
    ]