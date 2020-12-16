# Generated by Django 3.1.4 on 2020-12-11 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pluginServer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='Toatl_DayTime',
            new_name='cDayTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='Toatl_WeekTime',
            new_name='cppDayTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='haskell_DayTime',
            new_name='goDayTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='haskell_WeekTime',
            new_name='haskellDayTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='java_DayTime',
            new_name='javaDayTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='java_WeekTime',
            new_name='jsDayTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='kotlin_DayTime',
            new_name='kotlinDayTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='kotlin_WeekTime',
            new_name='otherDayTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='other_DayTime',
            new_name='pythonDayTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='other_WeekTime',
            new_name='rustDayTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='python_DayTime',
            new_name='rustWeekTime',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='python_WeekTime',
            new_name='totalDayTime',
        ),
        migrations.RemoveField(
            model_name='time',
            name='rust_DayTime',
        ),
        migrations.RemoveField(
            model_name='time',
            name='rust_WeekTime',
        ),
    ]