# Generated by Django 5.0 on 2023-12-28 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0004_alter_simulation_phase'),
    ]

    operations = [
        migrations.AddField(
            model_name='glip',
            name='partner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='simulation.glip'),
        ),
    ]