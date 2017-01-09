# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 04:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtools', '0003_auto_20160128_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Profile picture')),
                ('bio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Short Bio')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
                ('birthday', models.DateField(blank=True, default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
