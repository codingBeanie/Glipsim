import logging
import random
import time
import simulation.parameters as PARAM
from simulation.models import *
from simulation.name_generator import NameGenerator
import simulation.phases.evaluation as phase_evaluation
from simulation.phases.aging import aging
from simulation.events.dating import dating
from simulation.events.mating import mating
from simulation.events.statistics import gather_statistics

logger = logging.getLogger("sim")


def simulation_restart():
    logger.info("Simulation restarted")

    logger.info("Delete all Models")
    Glip.objects.all().delete()
    Simulation.objects.all().delete()
    Statistics.objects.all().delete()
    Household.objects.all().delete()

    logger.info("Create initial Glip population")
    name_generator = NameGenerator()

    for i in range(PARAM.SETUP_GLIP_COUNT):
        family_name = name_generator.generate_family_name()
        child_name = name_generator.generate_child_name(0)
        first_name = family_name[0]
        second_name = family_name[1]
        full_name = first_name + second_name + child_name
        age = random.randint(PARAM.SETUP_MIN_AGE,
                             PARAM.SETUP_MAX_AGE)
        dna = ""
        for d in range(PARAM.SETUP_DNA_LENGTH):
            gen_choice = random.choice(["0", "1"])
            dna += gen_choice

        glip = Glip(first_name=first_name, second_name=second_name, child_name=child_name,
                    full_name=full_name, dna=dna, age=age, action="idle", adult=True, alive=True, health=PARAM.GLIP_MAX_HEALTH)
        glip.save()

        household = Household(name=first_name + second_name,
                              resources=PARAM.GLIP_START_RESOURCES)
        household.save()

        glip.household = household
        glip.save()

    logger.info(f"Initial Glip population of {
                PARAM.SETUP_GLIP_COUNT} created")

    logger.info("Create initial Simulation")
    simulation = Simulation(phase=1, tick=0)
    simulation.save()
    statistics = Statistics(tick=0, population=PARAM.SETUP_GLIP_COUNT)
    statistics.save()
    logger.info("Setup finished")


def simulation_run():
    logger.info("Simulation started")
    simulation = Simulation.objects.first()
    statistics = Statistics.objects.first()
    logger.info(f"Simulation phase: {
                str(simulation.phase)} @ tick: {str(simulation.tick)} with Population {str(statistics.population)}")

    # start simulation loop
    while simulation.tick < PARAM.SIM_MAX_TICK and statistics.population >= PARAM.SIM_MIN_POPULATION and statistics.population <= PARAM.SIM_MAX_POPULATION:
        logger.info(f"Simulation tick: {simulation.tick}")
        begin_time = time.time()
        if simulation.tick > 0:
            statistics = Statistics(tick=simulation.tick)
            statistics.save()

        # evaluation phase
        if simulation.phase == 1:
            phase_evaluation.evaluation()
            simulation.phase += 1
            simulation.save()

        # event phase
        if simulation.phase == 2:
            dating()
            mating(statistics)
            simulation.phase += 1
            simulation.save()

        # aging phase
        if simulation.phase == 3:
            aging(statistics)
            simulation.phase += 1
            simulation.save()

        # gather statistics and save it to model
        if simulation.phase == 4:
            statistics.population = Glip.objects.filter(alive=True).count()
            statistics.save()
            if statistics.population > 0:
                gather_statistics(statistics, simulation.tick)
            simulation.phase += 1
            simulation.save()

        # uptick and phase reset
        simulation.tick += 1
        simulation.phase = 1
        simulation.save()
        end_time = time.time()
        elapsed_time = int(round((end_time - begin_time) * 1000, 0))
        statistics.run_time = elapsed_time
        statistics.save()

    if statistics.population <= PARAM.SIM_MIN_POPULATION:
        logger.warning(f"Population Min Limit of {
            str(PARAM.SIM_MIN_POPULATION)} reached")
    if statistics.population >= PARAM.SIM_MAX_POPULATION:
        logger.warning(f"Population Max Limit of {
            str(PARAM.SIM_MAX_POPULATION)} reached")
    logger.info("Simulation ended")
