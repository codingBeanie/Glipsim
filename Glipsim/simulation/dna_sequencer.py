import simulation.parameters as PARAM
import random


class DNA_Sequencer:
    def __init__(self, dna_string):
        self.sequence = dna_string
        self.genes = {
            "appearance": self.sequence[0:3],
            "appearance_preference": self.sequence[3:6],
            "tolerance_dating": self.sequence[6:8],
            "tolerance_age": self.sequence[8:10],
            "evaluation_modifiers": self.sequence[10:(10 + PARAM.NUM_INPUTS * PARAM.NUM_OUTPUTS * PARAM.LEN_MODIFIER)],
        }

    def convert_to_list(self, sequence):
        result = []
        for s in sequence:
            result.append(int(s))
        return tuple(result)

    def get_appearance(self):
        return self.convert_to_list(self.genes["appearance"])

    def get_appearance_preference(self):
        return self.convert_to_list(self.genes["appearance_preference"])

    def get_tolerance_dating(self):
        # 0..3
        return int(self.genes["tolerance_dating"], 2)

    def get_tolerance_age(self):
        gencode = int(self.genes["tolerance_age"], 2)
        if gencode == 0:
            tolerance_age = PARAM.GLIP_TOLERANCE_AGE_CASE_YOUNGER
        elif gencode == 1:
            tolerance_age = PARAM.GLIP_TOLERANCE_AGE_CASE_OLDER
        else:
            tolerance_age = PARAM.GLIP_TOLERANCE_AGE_CASE_SIMILIAR
        return tolerance_age

    def get_health_modifier(self):
        gencode = int(self.genes["reproduction_modifier"], 2)    # 0..15
        return gencode - 7  # -7..8

    def gen_as_int(self, gen):
        return int(self.genes[gen], 2)


def dna_recombination(dna1, dna2):
    new_dna = ""
    for gen in dna1.genes.items():
        new_dna += random.choice([gen[1], dna2.genes[gen[0]]])

    # mutation
    for gen in range(len(new_dna)):
        if random.randint(1, 10000) <= PARAM.REPRODUCTION_MUTATION_CHANCE:
            new_dna = new_dna[:gen] + \
                str(random.randint(0, 1)) + new_dna[gen+1:]
    return new_dna
