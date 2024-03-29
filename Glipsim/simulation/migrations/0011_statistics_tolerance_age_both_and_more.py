# Generated by Django 5.0 on 2024-01-08 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0010_statistics_preference_black_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='tolerance_age_both',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='tolerance_age_high',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='tolerance_age_low',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='tolerance_age_med',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='tolerance_dating_0',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='tolerance_dating_1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='tolerance_dating_2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='tolerance_dating_3',
            field=models.FloatField(default=0),
        ),
    ]
