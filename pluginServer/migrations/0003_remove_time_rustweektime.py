# Generated by Django 3.1.4 on 2020-12-12 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pluginServer', '0002_auto_20201211_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='rustWeekTime',
        ),
    ]