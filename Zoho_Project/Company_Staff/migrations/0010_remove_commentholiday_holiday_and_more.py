# Generated by Django 5.0 on 2024-02-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0009_commentholiday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentholiday',
            name='holiday',
        ),
        migrations.AddField(
            model_name='commentholiday',
            name='holidaymonth',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]