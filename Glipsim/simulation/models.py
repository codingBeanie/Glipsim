from django.db import models
import simulation.parameters as PARAM


class Glip(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    child_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=20)
    dna = models.CharField(max_length=PARAM.SETUP_DNA_LENGTH)

    age = models.IntegerField(default=20)
    action = models.CharField(max_length=20, default="idle")
    adult = models.BooleanField(default=False)
    health = models.IntegerField(default=100)
    alive = models.BooleanField(default=True)
    death_tick = models.IntegerField(default=None, null=True)

    partner = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, default=None)
    parents = models.ManyToManyField(
        'self', related_name='children', symmetrical=False, blank=True)
    household = models.ForeignKey(
        'Household', on_delete=models.CASCADE, null=True, default=None)


class Household(models.Model):
    name = models.CharField(max_length=20)
    resources = models.IntegerField(default=0)


class Simulation(models.Model):
    phase = models.IntegerField(default=0)
    tick = models.IntegerField(default=0)


class Statistics(models.Model):
    tick = models.IntegerField(default=0)
    population = models.IntegerField(default=0)
    births = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)

    appearance_red = models.FloatField(default=0)
    appearance_blue = models.FloatField(default=0)
    appearance_green = models.FloatField(default=0)
    appearance_yellow = models.FloatField(default=0)
    appearance_turq = models.FloatField(default=0)
    appearance_pink = models.FloatField(default=0)
    appearance_black = models.FloatField(default=0.0)
    appearance_white = models.FloatField(default=0)

    preference_red = models.FloatField(default=0)
    preference_blue = models.FloatField(default=0)
    preference_green = models.FloatField(default=0)
    preference_yellow = models.FloatField(default=0)
    preference_turq = models.FloatField(default=0)
    preference_pink = models.FloatField(default=0)
    preference_black = models.FloatField(default=0)
    preference_white = models.FloatField(default=0)

    tolerance_dating_0 = models.FloatField(default=0)
    tolerance_dating_1 = models.FloatField(default=0)
    tolerance_dating_2 = models.FloatField(default=0)
    tolerance_dating_3 = models.FloatField(default=0)

    tolerance_age_younger = models.FloatField(default=0)
    tolerance_age_similiar = models.FloatField(default=0)
    tolerance_age_older = models.FloatField(default=0)

    average_health = models.FloatField(default=0)

    average_death_age = models.FloatField(default=0)

    action_idle = models.IntegerField(default=0)
    action_mating = models.IntegerField(default=0)
    action_dating = models.IntegerField(default=0)

    run_time = models.IntegerField(default=0)
