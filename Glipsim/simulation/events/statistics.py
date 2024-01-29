from simulation.models import Statistics, Glip
from simulation.dna_sequencer import DNA_Sequencer
import simulation.parameters as PARAM
from django.db.models import Q


def gather_statistics(statistics, tick):
    glips = Glip.objects.filter(alive=True)
    healths = []
    death_ages = []

    for glip in glips:
        dna = DNA_Sequencer(glip.dna)

        # count appearance
        appearance = dna.get_appearance()
        if appearance == (0, 0, 0):
            statistics.appearance_black += 1
        if appearance == (1, 0, 0):
            statistics.appearance_red += 1
        if appearance == (0, 1, 0):
            statistics.appearance_green += 1
        if appearance == (0, 0, 1):
            statistics.appearance_blue += 1
        if appearance == (1, 1, 0):
            statistics.appearance_yellow += 1
        if appearance == (0, 1, 1):
            statistics.appearance_turq += 1
        if appearance == (1, 0, 1):
            statistics.appearance_pink += 1
        if appearance == (1, 1, 1):
            statistics.appearance_white += 1

        # count preference
        preference = dna.get_appearance_preference()
        if preference == (0, 0, 0):
            statistics.preference_black += 1
        if preference == (1, 0, 0):
            statistics.preference_red += 1
        if preference == (0, 1, 0):
            statistics.preference_green += 1
        if preference == (0, 0, 1):
            statistics.preference_blue += 1
        if preference == (1, 1, 0):
            statistics.preference_yellow += 1
        if preference == (0, 1, 1):
            statistics.preference_turq += 1
        if preference == (1, 0, 1):
            statistics.preference_pink += 1
        if preference == (1, 1, 1):
            statistics.preference_white += 1

        # tolerance dating
        tolerance_dating = dna.get_tolerance_dating()
        if tolerance_dating == 0:
            statistics.tolerance_dating_0 += 1
        if tolerance_dating == 1:
            statistics.tolerance_dating_1 += 1
        if tolerance_dating == 2:
            statistics.tolerance_dating_2 += 1
        if tolerance_dating == 3:
            statistics.tolerance_dating_3 += 1

        # tolerance age
        tolerance_age = int(dna.genes["tolerance_age"], 2)
        if tolerance_age == 0:
            statistics.tolerance_age_younger += 1
        if tolerance_age == 1:
            statistics.tolerance_age_older += 1
        if tolerance_age >= 2:
            statistics.tolerance_age_similiar += 1

        # average health
        healths.append(glip.health)

        # action
        if glip.action == "idle":
            statistics.action_idle += 1
        if glip.action == "mating":
            statistics.action_mating += 1
        if glip.action == "dating":
            statistics.action_dating += 1

    ##################################################################################
    # Relatives
    ##################################################################################

    count_total = glips.count()

    # calculate relative appearance
    statistics.appearance_black = round(
        statistics.appearance_black / count_total * 100, 2)
    statistics.appearance_red = round(
        statistics.appearance_red / count_total * 100, 2)
    statistics.appearance_green = round(
        statistics.appearance_green / count_total * 100, 2)
    statistics.appearance_yellow = round(
        statistics.appearance_yellow / count_total * 100, 2)
    statistics.appearance_blue = round(
        statistics.appearance_blue / count_total * 100, 2)
    statistics.appearance_turq = round(
        statistics.appearance_turq / count_total * 100, 2)
    statistics.appearance_pink = round(
        statistics.appearance_pink / count_total * 100, 2)
    statistics.appearance_white = round(
        statistics.appearance_white / count_total * 100, 2)

    # calculate relative preference
    statistics.preference_black = round(
        statistics.preference_black / count_total * 100, 2)
    statistics.preference_red = round(
        statistics.preference_red / count_total * 100, 2)
    statistics.preference_green = round(
        statistics.preference_green / count_total * 100, 2)
    statistics.preference_yellow = round(
        statistics.preference_yellow / count_total * 100, 2)
    statistics.preference_blue = round(
        statistics.preference_blue / count_total * 100, 2)
    statistics.preference_turq = round(
        statistics.preference_turq / count_total * 100, 2)
    statistics.preference_pink = round(
        statistics.preference_pink / count_total * 100, 2)
    statistics.preference_white = round(
        statistics.preference_white / count_total * 100, 2)

    # calculate relative tolerance dating
    statistics.tolerance_dating_0 = round(
        (statistics.tolerance_dating_0 / count_total) * 100, 2)
    statistics.tolerance_dating_1 = round(
        statistics.tolerance_dating_1 / count_total * 100, 2)
    statistics.tolerance_dating_2 = round(
        statistics.tolerance_dating_2 / count_total * 100, 2)
    statistics.tolerance_dating_3 = round(
        statistics.tolerance_dating_3 / count_total * 100, 2)

    # calculate relative tolerance age
    statistics.tolerance_age_younger = round(
        statistics.tolerance_age_younger / count_total * 100, 2)
    statistics.tolerance_age_similiar = round(
        statistics.tolerance_age_similiar / count_total * 100, 2)
    statistics.tolerance_age_older = round(
        statistics.tolerance_age_older / count_total * 100, 2)

    # calculate average health
    statistics.average_health = round(sum(healths) / len(healths), 2)

    # calculate average death age
    dead_glips = Glip.objects.filter(Q(alive=False) & Q(
        death_tick__range=(tick-PARAM.DEATH_TIME_PERIOD, tick)))
    if dead_glips.count() > 0:
        statistics.average_death_age = round(
            sum([glip.age for glip in dead_glips]) / len(dead_glips), 2)
    else:
        statistics.average_death_age = 0

    # calculate action
    statistics.action_idle = round(
        statistics.action_idle / count_total * 100, 2)
    statistics.action_mating = round(
        statistics.action_mating / count_total * 100, 2)
    statistics.action_dating = round(
        statistics.action_dating / count_total * 100, 2)

    statistics.save()
