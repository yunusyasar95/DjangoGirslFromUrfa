# Generated by Django 2.0.13 on 2019-04-06 12:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 6, 12, 7, 42, 560028, tzinfo=utc)),
        ),
    ]