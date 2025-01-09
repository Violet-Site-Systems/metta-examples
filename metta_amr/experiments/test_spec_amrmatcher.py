import logging
import unittest
from metta_amr.metta_space import PatternParser, MettaSpace
from metta_amr.amr_processing import AmrProcessor, UtteranceParser
from metta_amr.amr_matching import AmrMatcher, AmrMatch

T = unittest.TestCase

class AmrMatcherTest(T):

    def setUp(self):
        self.amr_proc = AmrProcessor()
        self.work_space = MettaSpace()
        self.parser = PatternParser(self.work_space)

        self.input_space = MettaSpace()
        self.utterance_parser = UtteranceParser(self.amr_proc, self.input_space)
        self.matcher = AmrMatcher(self.work_space)

    # Rest of the code remains unchanged
