# Generated by Django 5.0 on 2024-02-10 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0004_comment_godown'),
        ('Register_Login', '0009_paymenttermsupdates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Godownhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('godown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.godown')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
    ]