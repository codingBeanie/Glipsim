from simulation.models import *
import simulation.parameters as PARAM
from simulation.dna_sequencer import DNA_Sequencer
import random
import logging
import math
logger = logging.getLogger("sim")


def dating():
    # select random dating glips
    glips = Glip.objects.filter(
        alive=True, adult=True, action="dating").order_by("?")
    num_pairs = len(glips) // 2

    # create dates
    for date in range(num_pairs):
        # get pair
        glip1 = glips[date*2]
        dna1 = DNA_Sequencer(glip1.dna)
        glip2 = glips[date*2+1]
        dna2 = DNA_Sequencer(glip2.dna)

        # check if sibbling
        glip1_parents = set(glip1.parents.all())
        glip2_parents = set(glip2.parents.all())
        if glip1_parents != set() and glip2_parents != set() and glip1_parents == glip2_parents:
            continue

        # get appearance, preference and tolerance
        glip1_appearance = dna1.get_appearance()
        glip1_preference = dna1.get_appearance_preference()
        glip1_tolerance_dating = dna1.get_tolerance_dating()
        glip2_appearance = dna2.get_appearance()
        glip2_preference = dna2.get_appearance_preference()
        glip2_tolerance_dating = dna2.get_tolerance_dating()

        # calculate attraction
        glip1_attraction = match_appearance_preference(
            glip2_appearance, glip1_preference)
        glip1_choice = True if glip1_attraction >= glip1_tolerance_dating else False
        glip2_attraction = match_appearance_preference(glip1_appearance,
                                                       glip2_preference)
        glip2_choice = True if glip2_attraction >= glip2_tolerance_dating else False

        # check age tolerances
        glip1_tolerance_age_min = dna1.get_tolerance_age()[0] + glip1.age
        glip1_tolerance_age_max = dna1.get_tolerance_age()[1] + glip1.age
        glip2_tolerance_age_min = dna2.get_tolerance_age()[0] + glip2.age
        glip2_tolerance_age_max = dna2.get_tolerance_age()[1] + glip2.age

        if glip1_tolerance_age_min > glip2.age or glip1_tolerance_age_max < glip2.age:
            glip1_age_choice = False
        else:
            glip1_age_choice = True
        if glip2_tolerance_age_min > glip1.age or glip2_tolerance_age_max < glip1.age:
            glip2_age_choice = False
        else:
            glip2_age_choice = True

        # if both glips are attracted to each other and the age tolerance is in bounds, they will become a couple
        if glip1_choice and glip2_choice and glip1_age_choice and glip2_age_choice:
            glip1.partner = glip2
            glip2.partner = glip1

            # remove from current household and transfer a share of the resources
            glip1_household = glip1.household
            glip2_household = glip2.household

            glip1_household_size = Glip.objects.filter(
                household=glip1_household).count()
            glip2_household_size = Glip.objects.filter(
                household=glip2_household).count()

            glip1_resources = math.floor(
                glip1_household.resources / glip1_household_size)
            glip2_resources = math.floor(
                glip2_household.resources / glip2_household_size)

            resources = glip1_resources + glip2_resources

            # create new household
            household = Household(name=glip1.first_name +
                                  glip2.second_name, resources=resources)
            household.save()
            glip1.household = household
            glip2.household = household

            glip1.save()
            glip2.save()
            logger.debug(f"{glip1.full_name} and {glip2.full_name} coupled")

    # set actions to idle
    for glip in glips:
        glip.save()


def match_appearance_preference(appearance, preference):
    match = 0
    for i in range(len(appearance)):
        if appearance[i] == preference[i]:
            match += 1
    return match
