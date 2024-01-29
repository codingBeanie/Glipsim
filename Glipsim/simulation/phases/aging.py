from simulation.models import Glip
from simulation.probabilities import *
from simulation.dna_sequencer import DNA_Sequencer
import simulation.parameters as PARAM
import random
import numpy as np
import logging

logger = logging.getLogger("sim")


def aging(statistics):
    glips = Glip.objects.filter(alive=True)
    deaths = 0
    for index, glip in enumerate(glips):
        dna_sequencer = DNA_Sequencer(glip.dna)
        glip.age += 1

        health_modifier = np.interp(
            glip.health, [0, PARAM.GLIP_MAX_HEALTH], PARAM.INTERP_HEALTH)
        survivability = int(probability_surviving(
            glip.age + health_modifier) * 1000)

        flip = random.randint(1, 1000)
        if flip < survivability:
            # survived
            glip.alive = True
            glip.adult = True if glip.age >= PARAM.GLIP_ADULT_AGE else False
        else:
            # died
            glip.alive = False
            glip.death_tick = statistics.tick
            deaths += 1
            logger.debug(f"{glip.full_name} died at age {glip.age}")

        glip.save()

    statistics.deaths = deaths
    statistics.save()
