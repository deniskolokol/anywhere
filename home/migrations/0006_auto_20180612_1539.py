# Generated by Django 2.0.6 on 2018-06-12 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180608_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floodmappage',
            name='country',
        ),
        migrations.RemoveField(
            model_name='floodmappage',
            name='date_from',
        ),
        migrations.RemoveField(
            model_name='floodmappage',
            name='date_to',
        ),
        migrations.RemoveField(
            model_name='floodmappage',
            name='flood_prob_threshold',
        ),
        migrations.RemoveField(
            model_name='floodmappage',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='floodmappage',
            name='time_from',
        ),
        migrations.RemoveField(
            model_name='floodmappage',
            name='time_range_text',
        ),
        migrations.RemoveField(
            model_name='floodmappage',
            name='time_to',
        ),
    ]