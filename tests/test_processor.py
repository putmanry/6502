# from architecture.processor import CPU_6502
import unittest
from architecture.processor import CPU_6502
import copy


class Test_LDAInstructions(unittest.TestCase):
    def setUp(self) -> None:
        self.processor = CPU_6502()
        self.processor.reset()
        self.processor.__str__()
        return super().setUp()

    def tearDown(self) -> None:
        del self.processor
        return super().tearDown()

    def checkRegisters(self, CPUCopy, ZFCopy=0, NFCopy=0):
        self.assertEqual(CPUCopy.CF, self.processor.CF, "CF not the same")
        self.assertEqual(CPUCopy.ID, self.processor.ID, "ID not the same")
        self.assertEqual(CPUCopy.DM, self.processor.DM, "DM not the same")
        self.assertEqual(CPUCopy.BC, self.processor.BC, "BC not the same")
        self.assertEqual(CPUCopy.OF, self.processor.OF, "OF not the same")

        self.assertEqual(self.processor.ZF, ZFCopy, "ZF not set correctly")
        self.assertEqual(self.processor.NF, NFCopy, "NF not set correctly")

    def test_LDAwithImmediate(self):

        # Inline program to test with
        self.processor.memory[0xFFFC] = 0xA9
        self.processor.memory[0xFFFD] = 0x82  # Tihs is the data we are loading into A

        # Check and see if NF is getting set correctly on a negative value
        CPUCopy = copy.deepcopy(self.processor)
        self.processor.LDA_Immediate(2)
        self.assertEqual(
            self.processor.A, 0x82, "LDAwithImmediate failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, 0, 1)

        # Check and see if NF is getting set correctly on a positive
        self.processor.reset()
        self.processor.memory[0xFFFD] = 0x32
        self.processor.LDA_Immediate(2)
        self.assertEqual(
            self.processor.A, 0x32, "LDAwithImmediate failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, 0, 0)

        # Check and see if ZF is getting set correctly
        self.processor.reset()
        self.processor.memory[0xFFFD] = 0x00
        self.processor.LDA_Immediate(2)
        self.assertEqual(
            self.processor.A, 0x00, "LDAwithImmediate failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, 1, 0)
        del CPUCopy

     def test_LDAwithZeroPage(self):
        # Inline program to test with
        self.processor.memory[0xFFFC] = 0xA5
        # Load from mem loc 0x10
        # Must be between 0x00 and 0xFF
        # For the locaion the MSB is always 0x00
        self.processor.memory[0xFFFD] = 0x00
        self.processor.memory[0x0000] = 0x10

        CPUCopy = copy.deepcopy(self.processor)
        
        self.processor.LDA_ZeroPage(3)
        assert self.processor.A == 0x10, "LDAwithZeroPage failed to load A correctly"
        self.checkRegisters(CPUCopy)
        del CPUCopy
