# Generated by Django 5.0 on 2024-02-14 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0011_commentholiday_holiday'),
    ]

    operations = [
        migrations.AddField(
            model_name='holiday',
            name='is_edited',
            field=models.BooleanField(default=False),
        ),
    ]