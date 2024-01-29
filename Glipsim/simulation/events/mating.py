import logging
import random
from simulation.dna_sequencer import DNA_Sequencer, dna_recombination
from simulation.models import Glip
from simulation.name_generator import NameGenerator
from simulation.probabilities import *
import simulation.parameters as PARAM
import numpy as np

logger = logging.getLogger("sim")


def mating(statistics):
    # select all mating glips
    glips = Glip.objects.filter(alive=True, adult=True, action="mating")
    births = 0
    name_generator = NameGenerator()
    logger.info(f"Mating started for {len(glips)}")

    for index, glip in enumerate(glips):
        # check if child was already made
        if glip.children.last() == None:
            mated = False
        elif glip.children.last().age == 0:
            mated = True
        else:
            mated = False

        if glip.partner.action == "mating" and glip.partner.alive and mated == False:
            # both glips are mating and no child was already made: try to create a child
            dna1 = DNA_Sequencer(glip.dna)
            dna2 = DNA_Sequencer(glip.partner.dna)
            modifier1 = np.interp(
                glip.health, [0, PARAM.GLIP_MAX_HEALTH], PARAM.INTERP_HEALTH)
            modifier2 = np.interp(glip.partner.health, [
                                  0, PARAM.GLIP_MAX_HEALTH], PARAM.INTERP_HEALTH)
            age1 = glip.age + modifier1
            age2 = glip.partner.age + modifier2

            probability1 = probability_reproduction(age1)
            probability2 = probability_reproduction(age2)
            probability = int((probability1 * probability2) * 100)
            logger.debug(f"Mating {
                glip.full_name} ({glip.age}) [{age1}] + {glip.partner.full_name} ({glip.partner.age}) [{age2}] with probability {probability}")

            if random.randint(0, probability) < PARAM.MATING_DC_ROLL:
                # new Glip is born
                births += 1
                child_name = name_generator.generate_child_name(
                    glip.children.count() + 1)
                first_name = glip.first_name
                second_name = glip.partner.second_name
                full_name = first_name + second_name + child_name
                age = 0
                dna = dna_recombination(dna1, dna2)
                logger.debug(f"{full_name} was born")
                child = Glip(first_name=first_name,
                             second_name=second_name,
                             child_name=child_name,
                             full_name=full_name,
                             dna=dna,
                             age=age,
                             action="idleing",
                             adult=False,
                             alive=True,
                             household=glip.household,
                             health=PARAM.GLIP_MAX_HEALTH)
                child.save()
                child.parents.add(glip.id)
                child.parents.add(glip.partner.id)
                child.save()
            else:
                # mating was unsuccesfulre
                pass

        else:
            # some alternative action will be here in future
            # keep in mind that the partner might already initiated the mating
            # and turned idle
            pass
        glip.save()

    statistics.births = births
    statistics.save()
