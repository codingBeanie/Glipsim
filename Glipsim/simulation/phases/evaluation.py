import simulation.parameters as PARAMS
import logging
from simulation.dna_sequencer import DNA_Sequencer
from simulation.models import Glip
import numpy as np
logger = logging.getLogger("sim")


def evaluation():
    logger.info("Phase evaluation started")
    # select all alive glips
    glips = Glip.objects.filter(alive=True, adult=True)

    # loop through all glips
    for glip in glips:
        # collect input variables
        age = int(
            np.clip(np.interp(glip.age, PARAMS.INTERP_AGE, PARAMS.INTERP_OUTPUT), 0, PARAMS.INTERP_OUTPUT[1]))
        children = int(np.clip(np.interp(glip.children.count(),
                                         PARAMS.INTERP_CHILDREN, PARAMS.INTERP_OUTPUT), 0, PARAMS.INTERP_OUTPUT[1]))
        resources = int(np.clip(np.interp(glip.household.resources,
                                          PARAMS.INTERP_RESOURCES, PARAMS.INTERP_OUTPUT), 0, PARAMS.INTERP_OUTPUT[1]))

        inputs = [age, children, resources]
        outputs = {"reproduction": 0, "working": 0, "idle": 0}
        dna_sequencer = DNA_Sequencer(glip.dna)
        modifier = dna_sequencer.genes["evaluation_modifiers"]
        print("length modifier: ", len(modifier))

        # calculate outputs values based on inputs and dna modifiers
        for index_output, output in enumerate(outputs.items()):
            for index_input, input in enumerate(inputs):
                # begin and end of the modifier gene
                beginnSlice = index_output * PARAMS.LEN_MODIFIER * \
                    PARAMS.NUM_INPUTS + index_input * PARAMS.LEN_MODIFIER
                endSlice = beginnSlice + PARAMS.LEN_MODIFIER

                modifier_slice = modifier[beginnSlice:endSlice]
                steepness_slice = modifier_slice[:4]
                halved_slice = modifier_slice[4:]

                steepness_value = int(steepness_slice, 2)   # 0..15
                halved_value = int(halved_slice, 2)         # 0..15

        # choose highest output value
        action = max(outputs, key=outputs.get)
        glip.action = action
        if action == "reproduction":
            if glip.partner != None:
                glip.action = "mating"
            else:
                glip.action = "dating"

        glip.save()
    logger.info("Phase evaluation finished")
