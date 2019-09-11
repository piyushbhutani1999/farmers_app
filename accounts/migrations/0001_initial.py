# Generated by Django 2.2.5 on 2019-09-11 20:50

import datetime
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('college_name', models.CharField(choices=[('', 'Select College'), ('nitkkr', 'NIT KURUKSHETRA'), ('thappar', 'THAPPAR , PATIALA')], default='', max_length=20)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=13, null=True, region='IN', unique=True)),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
