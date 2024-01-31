# Generated by Django 5.0 on 2024-01-31 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Register_Login', '0009_paymenttermsupdates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('holiday_name', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(max_length=255)),
                ('item_name', models.CharField(max_length=255)),
                ('hsn_code', models.IntegerField(blank=True, null=True)),
                ('tax_reference', models.CharField(max_length=255, null=True)),
                ('intrastate_tax', models.IntegerField(blank=True, null=True)),
                ('interstate_tax', models.IntegerField(blank=True, null=True)),
                ('selling_price', models.IntegerField(blank=True, null=True)),
                ('sales_account', models.CharField(max_length=255)),
                ('sales_description', models.CharField(max_length=255)),
                ('purchase_price', models.IntegerField(blank=True, null=True)),
                ('purchase_account', models.CharField(max_length=255)),
                ('purchase_description', models.CharField(max_length=255)),
                ('minimum_stock_to_maintain', models.IntegerField(blank=True, null=True)),
                ('inventory_account', models.CharField(max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('opening_stock', models.IntegerField(blank=True, default=0, null=True)),
                ('is_active', models.CharField(max_length=255, null=True)),
                ('current_stock', models.IntegerField(blank=True, default=0, null=True)),
                ('opening_stock_per_unit', models.IntegerField(blank=True, null=True)),
                ('track_inventory', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Godown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('HSN', models.CharField(max_length=255)),
                ('stock_in_hand', models.IntegerField()),
                ('godown_name', models.CharField(max_length=255)),
                ('godown_address', models.CharField(max_length=255)),
                ('stock_keeping', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='godowns', to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.items')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.unit'),
        ),
    ]
