# Generated by Django 5.0 on 2024-02-10 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0006_godown_is_edited_alter_godownhistory_company_and_more'),
        ('Register_Login', '0009_paymenttermsupdates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='godownhistory',
            name='login_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='godownhistory', to='Register_Login.logindetails'),
        ),
    ]