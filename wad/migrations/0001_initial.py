# Generated by Django 5.1.3 on 2024-11-17 04:06

import django.db.models.deletion
import django_better_admin_arrayfield.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True)),
                ('crop_duty_ft', models.FloatField()),
                ('area_enable', models.BooleanField(default=False)),
                ('crop_enable', models.BooleanField(default=False)),
                ('vol_enable', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True)),
                ('attn', models.CharField()),
                ('company', models.CharField()),
                ('address_1', models.CharField()),
                ('address_2', models.CharField()),
                ('city', models.CharField()),
                ('state', models.CharField()),
                ('zip', models.IntegerField()),
                ('home_phone', models.CharField()),
                ('office_phone', models.CharField()),
                ('mobile_phone', models.CharField()),
                ('fax', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('accounting_key', models.CharField()),
                ('active_date', models.DateField()),
                ('inactive_date', models.DateField()),
                ('active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(unique=True)),
                ('full_name', models.CharField()),
                ('address', models.CharField()),
                ('po_box', models.CharField()),
                ('city_state_zip', models.CharField()),
                ('office_phone', models.CharField()),
                ('office_email', models.EmailField(max_length=254)),
                ('office_fax', models.CharField()),
                ('website', models.URLField()),
                ('county', models.CharField()),
                ('country', models.CharField()),
                ('acreage', models.IntegerField(blank=True, null=True)),
                ('established', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.CharField()),
                ('description', models.CharField()),
                ('acres', models.FloatField()),
                ('irrig_acres', models.FloatField()),
                ('standby_acres', models.FloatField()),
                ('parcel_id', models.CharField()),
                ('vol_rate_adj_id', models.IntegerField()),
                ('active_date', models.DateField()),
                ('inactive_date', models.DateField()),
                ('active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('attributes', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, null=True, size=5)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RateAcre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acre_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RateStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('acre_basis', models.IntegerField()),
                ('acre_comp', models.BooleanField(default=False)),
                ('acre_due_mn', models.IntegerField()),
                ('acre_due_day', models.IntegerField()),
                ('acre_year_offset', models.IntegerField()),
                ('crop_comp', models.BooleanField(default=False)),
                ('crop_due_mn', models.IntegerField()),
                ('crop_due_day', models.IntegerField()),
                ('crop_year_offset', models.IntegerField()),
                ('vol_comp', models.BooleanField(default=False)),
                ('vol_due_mn', models.IntegerField()),
                ('vol_due_day', models.IntegerField()),
                ('vol_year_offset', models.IntegerField()),
                ('vol_start_mn', models.IntegerField()),
                ('vol_start_day', models.IntegerField()),
                ('vol_start_year_offset', models.IntegerField()),
                ('vol_end_mn', models.IntegerField()),
                ('vol_end_day', models.IntegerField()),
                ('vol_end_year_offset', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField()),
                ('role', models.CharField()),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qc_fall_start_mn', models.IntegerField()),
                ('qc_fall_start_dy', models.IntegerField()),
                ('qc_spring_start_mn', models.IntegerField()),
                ('qc_spring_start_dy', models.IntegerField()),
                ('use_wis', models.BooleanField(default=False)),
                ('district', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.district')),
            ],
        ),
        migrations.CreateModel(
            name='DistrictsAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField()),
                ('user', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('district', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.district')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_acres', models.FloatField()),
                ('acre_due_date', models.DateField()),
                ('total_acre_charge', models.FloatField()),
                ('total_crop_charge', models.FloatField()),
                ('crop_due_date', models.DateField()),
                ('total_vol_charge', models.FloatField()),
                ('total_vol_del', models.FloatField()),
                ('vol_due_date', models.DateField()),
                ('tot_vol_charge', models.FloatField()),
                ('total_charge', models.FloatField()),
                ('total_pay', models.FloatField()),
                ('total_adj', models.FloatField()),
                ('total_remain', models.FloatField()),
                ('is_vol_final', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('is_void', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('is_final', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('create_at', models.DateTimeField()),
                ('mod_at', models.DateTimeField()),
                ('comments', models.TextField()),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.customer')),
                ('rate', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.ratestructure')),
                ('service_year', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.serviceyear')),
            ],
        ),
        migrations.CreateModel(
            name='FieldInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acreage', models.FloatField()),
                ('pct_farmed', models.FloatField()),
                ('acre_rate', models.FloatField()),
                ('acre_charge', models.FloatField()),
                ('crop_rate', models.FloatField()),
                ('crop_charge', models.FloatField()),
                ('vol_start_date', models.DateField()),
                ('vol_end_date', models.DateField()),
                ('vol_rate', models.FloatField()),
                ('vol_del', models.FloatField()),
                ('vol_charge', models.FloatField()),
                ('field_charge', models.FloatField()),
                ('create_at', models.DateTimeField()),
                ('mod_at', models.DateTimeField()),
                ('crop', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.crop')),
                ('field', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.field')),
                ('invoice', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Adjustment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('is_void', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('mod_date', models.DateTimeField()),
                ('comments', models.TextField()),
                ('void_comments', models.TextField()),
                ('invoice', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('pay_number', models.IntegerField()),
                ('is_deposit', models.BooleanField()),
                ('is_void', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('create_at', models.DateTimeField()),
                ('mod_at', models.DateTimeField()),
                ('comments', models.TextField()),
                ('void_comments', models.TextField()),
                ('invoice', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='QCDailyField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('vol_af', models.FloatField()),
                ('method', models.IntegerField()),
                ('qc_flag', models.CharField()),
                ('field', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.field')),
            ],
        ),
        migrations.CreateModel(
            name='RateCrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_rate', models.FloatField()),
                ('crop_enabled', models.BooleanField()),
                ('crop', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.crop')),
            ],
        ),
        migrations.CreateModel(
            name='FieldCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_customer_id', models.IntegerField(blank=True, default=None, null=True)),
                ('service_year', models.DateField()),
                ('pct_farmed', models.FloatField()),
                ('comment', models.TextField(default='')),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.customer')),
                ('field', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.field')),
                ('rate', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.ratestructure')),
            ],
        ),
        migrations.CreateModel(
            name='RateVol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vol_rate_adj_id', models.IntegerField()),
                ('vol_rate', models.FloatField()),
                ('vol_enabled', models.BooleanField()),
                ('rate', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.ratestructure')),
            ],
        ),
        migrations.CreateModel(
            name='FieldCrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pct_planted', models.FloatField()),
                ('comment', models.TextField()),
                ('crop', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.crop')),
                ('field', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.field')),
                ('rate', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.ratestructure')),
                ('service_year', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.serviceyear')),
            ],
        ),
        migrations.CreateModel(
            name='VolDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vol_start_date', models.DateField()),
                ('vol_end_date', models.DateField()),
                ('mod_at', models.DateField()),
                ('comment', models.TextField()),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.customer')),
                ('field', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.field')),
                ('rate', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.ratestructure')),
                ('service_year', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wad.serviceyear')),
            ],
        ),
    ]