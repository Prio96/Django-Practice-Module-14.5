# Generated by Django 5.1 on 2024-09-04 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('bigautofield', models.BigAutoField(primary_key=True, serialize=False)),
                ('bank_balance', models.PositiveBigIntegerField(default=None)),
                ('name', models.CharField(default=None, max_length=70)),
                ('age', models.PositiveSmallIntegerField(default=None)),
                ('photo', models.BinaryField(default=None)),
                ('dateofbirth', models.DateField(default=datetime.date.today)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=5)),
                ('height', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('facebook_id', models.URLField()),
                ('ip', models.GenericIPAddressField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
