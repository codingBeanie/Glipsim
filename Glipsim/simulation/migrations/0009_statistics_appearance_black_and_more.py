# Generated by Django 5.0 on 2024-01-05 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0008_statistics_remove_simulation_births_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='appearance_black',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='appearance_blue',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='appearance_green',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='appearance_pink',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='appearance_red',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='appearance_turq',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='appearance_white',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='appearance_yellow',
            field=models.FloatField(default=0),
        ),
    ]
