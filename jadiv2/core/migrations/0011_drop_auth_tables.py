# core/migrations/0002_drop_auth_tables.py
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_coreuserprofile_table_alter_interest_table_and_more'),  # Update this with your actual initial migration
    ]

    operations = [
        migrations.RunSQL("DROP TABLE IF EXISTS auth_permission CASCADE;"),
        migrations.RunSQL("DROP TABLE IF EXISTS auth_group CASCADE;"),
        migrations.RunSQL("DROP TABLE IF EXISTS auth_group_permissions CASCADE;"),
        migrations.RunSQL("DROP TABLE IF EXISTS auth_user_groups CASCADE;"),
        migrations.RunSQL("DROP TABLE IF EXISTS auth_user_user_permissions CASCADE;"),
    ]

