# Generated by Django 5.0 on 2024-01-29 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0012_alter_godown_active_log'),
    ]

    operations = [
        migrations.RenameField(
            model_name='godown',
            old_name='active_log',
            new_name='activation_log',
        ),
    ]