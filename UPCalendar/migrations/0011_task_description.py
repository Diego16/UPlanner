# Generated by Django 2.2 on 2019-05-20 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPCalendar', '0010_auto_20190519_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]