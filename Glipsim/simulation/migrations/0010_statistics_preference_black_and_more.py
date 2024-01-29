# Generated by Django 5.0 on 2024-01-08 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0009_statistics_appearance_black_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='preference_black',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='preference_blue',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='preference_green',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='preference_pink',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='preference_red',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='preference_turq',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='preference_white',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='preference_yellow',
            field=models.FloatField(default=0),
        ),
    ]
