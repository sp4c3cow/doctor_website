# Generated by Django 3.1.2 on 2020-11-06 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20201106_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]