# from architecture.processor import CPU_6502
import unittest
from architecture.processor import CPU_6502
import copy


class Test_LDAInstructions(unittest.TestCase):
    def setUp(self) -> None:
        print("\n*************** New Test Run ****************")
        self.processor = CPU_6502()
        self.processor.reset()
        # self.processor.__str__()
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

    def programSetup(self, instructions):
        self.processor.reset()
        # Inline program to test with
        for i in range(len(instructions)):
            self.processor.memory[instructions[i][0]] = instructions[i][1]

    def test_LDAwithImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Check and see if NF is getting set correctly on a negative value
        # ZF should not change
        instructions = ([0xFFFC, 0xA8], [0xFFFD, 0x82])
        self.programSetup(instructions)
        self.processor.LDA_Immediate(2)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDAwithImmediate failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Check and see if NF is not chaning on a positive load
        # ZF does not change.
        instructions = ([0xFFFC, 0xA8], [0xFFFD, 0x32])
        self.programSetup(instructions)
        self.processor.LDA_Immediate(2)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDAwithImmediate failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        # Test 3 - Check and see if ZF is getting set correctly
        # NF should not change
        instructions = ([0xFFFC, 0xA8], [0xFFFD, 0x00])
        self.programSetup(instructions)
        self.processor.LDA_Immediate(2)
        self.assertEqual(
            self.processor.A, 0x00, "3 - LDAwithImmediate failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)
        print("Complete: test_LDAwithImmediate =======")
        del CPUCopy

    def test_LDAwithZeroPage(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Load from mem loc 0x10 Must be between 0x00 and 0xFF
        # For the locaion the MSB is always 0x00
        # For 0x82 - ZF should not change and NF get set
        instructions = ([0xFFFC, 0xA5], [0xFFFD, 0x00], [0x0000, 0x82])
        self.programSetup(instructions)
        self.processor.LDA_ZeroPage(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDAwithZeroPage failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xA5], [0xFFFD, 0x00], [0x0000, 0x32])
        self.programSetup(instructions)
        self.processor.LDA_ZeroPage(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDAwithZeroPage failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 2 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xA5], [0xFFFD, 0x00], [0x0000, 0x00])
        self.programSetup(instructions)
        self.processor.LDA_ZeroPage(3)
        self.assertEqual(
            self.processor.A, 0x00, "2 - LDAwithZeroPage failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        print("Complete: test_LDAwithZeroPage =======")
        del CPUCopy

    def test_ZeroPageWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Load from mem loc 0x10 Must be between 0x00 and 0xFF
        # If X contains 0x0F and the ins is LDA $80,X then A is loaded
        #    from 0x008F (0x80 + 0x0F)
        # For 0x82 - ZF should not change and NF get set
        instructions = ([0xFFFC, 0xB5], [0xFFFD, 0x80], [0x008F, 0x82])
        self.processor.X = 0x0F
        self.programSetup(instructions)
        self.processor.LDA_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDAwithZeroPageWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xB5], [0xFFFD, 0x80], [0x008F, 0x32])
        self.processor.X = 0x0F
        self.programSetup(instructions)
        self.processor.LDA_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDAwithZeroPageWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 3 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xB5], [0xFFFD, 0x80], [0x008F, 0x00])
        self.processor.X = 0x0F
        self.programSetup(instructions)
        self.processor.LDA_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A, 0x00, "2 - LDAwithZeroPageWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # TODO: need to deal with wrapping at top end.

        print("Complete: test_LDAwithZeroPageWithX =======")
        del CPUCopy

    def test_LDAwithAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Load from mem loc 0x10 Must be between 0x00 and 0xFF
        # For the locaion the MSB is always 0x00
        # For 0x82 - ZF should not change and NF get set
        instructions = ([0xFFFC, 0xAD], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x4480, 0x82])
        self.programSetup(instructions)
        self.processor.LDA_Absolute(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDAwithAbsolute failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xAD], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x4480, 0x32])
        self.programSetup(instructions)
        self.processor.LDA_Absolute(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDAwithAbsolute failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 2 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xAD], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x4480, 0x00])
        self.programSetup(instructions)
        self.processor.LDA_Absolute(3)
        self.assertEqual(
            self.processor.A, 0x00, "2 - LDAWithAbsolute failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        print("Complete: test_LDAwithAbsolute =======")
        del CPUCopy
