# Generated by Django 5.0 on 2024-01-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0014_alter_items_activation_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='godown',
            old_name='activation_log',
            new_name='is_active',
        ),
        migrations.RemoveField(
            model_name='items',
            name='activation_tag',
        ),
        migrations.AddField(
            model_name='items',
            name='is_active',
            field=models.IntegerField(default=0),
        ),
    ]
