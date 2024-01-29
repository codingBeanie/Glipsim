# Generated by Django 5.0 on 2024-01-08 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0011_statistics_tolerance_age_both_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='age_modifier_avg',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='age_modifier_median',
            field=models.FloatField(default=0),
        ),
    ]