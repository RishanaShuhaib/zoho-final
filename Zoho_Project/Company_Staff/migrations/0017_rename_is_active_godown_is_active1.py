# Generated by Django 5.0 on 2024-01-29 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0016_alter_items_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='godown',
            old_name='is_active',
            new_name='is_active1',
        ),
    ]