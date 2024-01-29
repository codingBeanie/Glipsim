# SETUP
SETUP_MIN_AGE = 18
SETUP_MAX_AGE = 24
SETUP_GLIP_COUNT = 50
SETUP_DNA_LENGTH = 82

# SIMULATION
SIM_MAX_TICK = 30
SIM_MIN_POPULATION = 1
SIM_MAX_POPULATION = 1000

# GLIP
GLIP_ADULT_AGE = 18
GLIP_TOLERANCE_AGE_CASE_YOUNGER = (-30, -5)
GLIP_TOLERANCE_AGE_CASE_SIMILIAR = (-10, 10)
GLIP_TOLERANCE_AGE_CASE_OLDER = (5, 30)
GLIP_START_RESOURCES = 5
GLIP_MAX_HEALTH = 10
INTERP_HEALTH = [15, -15]

# EVALUATION
INTERP_OUTPUT = [0, 10]  # value range to which each input is scaled
INTERP_RESOURCES = [0, 100]  # base range of resources (min, max)
INTERP_CHILDREN = [0, 10]  # base range of children (min, max)
INTERP_AGE = [0, 90]  # base range of age (min, max)
INTERP_GENE = [0, 15]  # base range of gene modifier (min, max)
INTERP_STEEPNESS = [0, 2]  # range of steepness (min, max)
INTERP_HALVED = [0, 10]  # range of halved (min, max)


# EVALUATION GENES
NUM_INPUTS = 3     # age, resources, children
NUM_OUTPUTS = 3    # reproduction, working, idleing
# 4 bit for steepness (0..15) -> 16 steps, 4 bit for halved (0..15) -> 16 steps
LEN_MODIFIER = 8


# MATING
MATING_DC_ROLL = 100  # GLips roll 1..100, if roll < DC_ROLL, mating is successful
REPRODUCTION_MUTATION_CHANCE = 10  # chance to 10.000

# STATISTICS
DEATH_TIME_PERIOD = 0
