# Generated by Django 5.0 on 2024-02-12 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0008_alter_godownhistory_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentHoliday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('holiday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.holiday')),
            ],
        ),
    ]
