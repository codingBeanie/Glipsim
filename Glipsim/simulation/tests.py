from django.test import TestCase
from simulation.dna_sequencer import DNA_Sequencer
import simulation.PARAM as PARAM
from simulation.events.dating import match_appearance_preference
import random


class Test_DNA_Sequencer(TestCase):
    def test_sequencing(self):
        dna = "1234567890"
        dna_sequencer = DNA_Sequencer(dna)

        self.assertEqual(dna_sequencer.genes, dna)
        self.assertEqual(dna_sequencer.gen_appearance, "123")
        self.assertEqual(dna_sequencer.gen_appearance_preference, "456")
        self.assertEqual(dna_sequencer.gen_tolerance_dating, "7")

    def test_translations(self):
        dna = "ATCGATCGATCG"
        dna_sequencer = DNA_Sequencer(dna)

        self.assertEqual(dna_sequencer.get_appearance(), [0, 0, 1])
        self.assertEqual(dna_sequencer.get_appearance_preference(), [1, 0, 0])

    def test_converter(self):
        dna = ""
        for d in range(PARAM.SETUP_DNA_LENGTH):
            gen_choice = random.choice(["A", "T", "C", "G"])
            dna += gen_choice

        dna_sequencer = DNA_Sequencer(dna)
        self.assertEqual(dna_sequencer.convert_to_decimal("AAAA"), 0)
        self.assertEqual(dna_sequencer.convert_to_decimal("AATT"), 2)
        self.assertEqual(dna_sequencer.convert_to_decimal("TTTT"), 4)
        self.assertEqual(dna_sequencer.convert_to_decimal("TTAA"), 2)
        self.assertEqual(dna_sequencer.convert_to_decimal("TTCC"), 6)
        self.assertEqual(dna_sequencer.convert_to_decimal("CCCC"), 8)
        self.assertEqual(dna_sequencer.convert_to_decimal("ATCG"), 6)
        self.assertEqual(dna_sequencer.convert_to_decimal("CCGG"), 10)

    def test_reproduction_modifier(self):
        dna = ""
        for d in range(PARAM.SETUP_DNA_LENGTH):
            gen_choice = random.choice(["A", "T", "C", "G"])
            dna += gen_choice

        dna = dna[:8] + "AAAA" + dna[14:]
        dna_sequencer = DNA_Sequencer(dna)
        self.assertEqual(dna_sequencer.get_health_modifier(), -6)

        dna = dna[:8] + "TTTT" + dna[14:]
        dna_sequencer = DNA_Sequencer(dna)
        self.assertEqual(dna_sequencer.get_health_modifier(), -2)

        dna = dna[:8] + "CCCC" + dna[14:]
        dna_sequencer = DNA_Sequencer(dna)
        self.assertEqual(dna_sequencer.get_health_modifier(), 2)

        dna = dna[:8] + "GGGG" + dna[14:]
        dna_sequencer = DNA_Sequencer(dna)
        self.assertEqual(dna_sequencer.get_health_modifier(), 6)


class Test_Dating(TestCase):
    def test_matching(self):
        appearance = [1, 1, 1]
        preference = [1, 1, 1]
        self.assertEqual(match_appearance_preference(
            appearance, preference), 3)

        appearance = [1, 1, 1]
        preference = [0, 1, 1]
        self.assertEqual(match_appearance_preference(
            appearance, preference), 2)

        appearance = [1, 1, 1]
        preference = [0, 0, 1]
        self.assertEqual(match_appearance_preference(
            appearance, preference), 1)

        appearance = [1, 1, 1]
        preference = [0, 0, 0]
        self.assertEqual(match_appearance_preference(
            appearance, preference), 0)
