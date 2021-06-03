# from architecture.processor import CPU_6502
import unittest
from architecture.processor import CPU_6502


class Test_LDAInstructions(unittest.TestCase):
    def setUp(self) -> None:
        self.processor = CPU_6502()
        self.processor.reset()
        self.processor.__str__()
        return super().setUp()

    def tearDown(self) -> None:
        del self.processor
        return super().tearDown()

    def test_LDAwithImmediate(self):
        # Inline program to test with
        self.processor.memory[0xFFFC] = 0xA9
        self.processor.memory[0xFFFD] = 0x42
        self.processor.LDA_Immediate(2)
        assert self.processor.A == 0x42, "LDAwithIM failed to load A correctly"

    def test_LDAwithAbsolute(self):
        pass
