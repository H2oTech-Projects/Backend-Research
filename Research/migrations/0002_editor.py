# Generated by Django 5.1.4 on 2025-01-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('name_of_book', models.CharField(max_length=20)),
            ],
        ),
    ]
