# Generated by Django 5.0 on 2024-01-29 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0004_alter_holiday_end_date_alter_holiday_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]