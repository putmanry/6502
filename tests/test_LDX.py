# from architecture.processor import CPU_6502
import unittest
import copy
from architecture._base_instruction import _BaseInstruction


class Test_LDXInstructions(_BaseInstruction, unittest.TestCase):
    def __init__(self):
        super().__init__()


"""
    def test_LDXwithImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Check and see if NF is getting set correctly on a negative value
        # ZF should not change
        instructions = ([0xFFFC, 0xA2], [0xFFFD, 0x82])
        self.programSetup(instructions)
        self.processor.LDX_Immediate(2)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDXwithImmediate failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Check and see if NF is not chaning on a positive load
        # ZF does not change.
        instructions = ([0xFFFC, 0xA2], [0xFFFD, 0x32])
        self.programSetup(instructions)
        self.processor.LDX_Immediate(2)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDXwithImmediate failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        # Test 3 - Check and see if ZF is getting set correctly
        # NF should not change
        instructions = ([0xFFFC, 0xA2], [0xFFFD, 0x00])
        self.programSetup(instructions)
        self.processor.LDX_Immediate(2)
        self.assertEqual(
            self.processor.A, 0x00, "3 - LDXwithImmediate failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)
        print("Complete: test_LDXwithImmediate =======")
        del CPUCopy

"""
"""
    def test_LDXwithZeroPage(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Load from mem loc 0x10 Must be between 0x00 and 0xFF
        # For the locaion the MSB is always 0x00
        # For 0x82 - ZF should not change and NF get set
        instructions = ([0xFFFC, 0xA6], [0xFFFD, 0x00], [0x0000, 0x82])
        self.programSetup(instructions)
        self.processor.LDX_ZeroPage(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDXwithZeroPage failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xA6], [0xFFFD, 0x00], [0x0000, 0x32])
        self.programSetup(instructions)
        self.processor.LDX_ZeroPage(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDXwithZeroPage failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 2 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xA6], [0xFFFD, 0x00], [0x0000, 0x00])
        self.programSetup(instructions)
        self.processor.LDX_ZeroPage(3)
        self.assertEqual(
            self.processor.A, 0x00, "2 - LDXwithZeroPage failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        print("Complete: test_LDXwithZeroPage =======")
        del CPUCopy

    def test_LDXwithZeroPageY(self):
        return True

    def test_LDXwithAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Instruction contains the full 16 bit address to the identify the target location
        instructions = ([0xFFFC, 0xAE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x4480, 0x82])
        self.programSetup(instructions)
        self.processor.LDX_Absolute(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDXwithAbsolute failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xAE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x4480, 0x32])
        self.programSetup(instructions)
        self.processor.LDX_Absolute(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDXwithAbsolute failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 2 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xAE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x4480, 0x00])
        self.programSetup(instructions)
        self.processor.LDX_Absolute(3)
        self.assertEqual(
            self.processor.A, 0x00, "2 - LDXWithAbsolute failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        print("Complete: test_LDXwithAbsolute =======")
        del CPUCopy

    def test_AbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # If X containes 0x92 and we have an LDX 0x2000, X the instruction will load from
        # 0x2092.
        instructions = ([0xFFFC, 0xBE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x82])
        self.processor.Y = 0x0F
        self.programSetup(instructions)
        self.processor.LDX_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDXAbsoluteWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xBE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x32])
        self.processor.Y = 0x0F
        self.programSetup(instructions)
        self.processor.LDX_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDXAbsoluteWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 3 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xBE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x00])
        self.processor.Y = 0x0F
        self.programSetup(instructions)
        self.processor.LDX_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A, 0x00, "2 - LDXAbsoluteWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # TODO: need to deal with wrapping at top end.

        print("Complete: LDXAbsoluteWithY=======")
        del CPUCopy
"""
