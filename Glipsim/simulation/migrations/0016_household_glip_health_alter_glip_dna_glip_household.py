# Generated by Django 5.0 on 2024-01-18 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0015_rename_tolerance_age_both_statistics_tolerance_age_older_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('resources', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='glip',
            name='health',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='glip',
            name='dna',
            field=models.CharField(max_length=44),
        ),
        migrations.AddField(
            model_name='glip',
            name='household',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='simulation.household'),
        ),
    ]
