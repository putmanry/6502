import unittest
from architecture.processor import CPU_6502
import copy
import datetime
import _BaseTest

"""
LDX - Load X Register			
			
X,Z,N = M			
			
Loads a byte of memory into the X register setting the zero and negative flags as appropriate.			
			
C	Carry Flag	Not affected	
Z	Zero Flag	Set if X = 0	
I	Interrupt Disable	Not affected	
D	Decimal Mode Flag	Not affected	
B	Break Command	Not affected	
V	Overflow Flag	Not affected	
N	Negative Flag	Set if bit 7 of X is set	
			
Addressing Mode	Opcode	Bytes	Cycles
Immediate	$A2	2	2
Zero Page	$A6	2	3
Zero Page,Y	$B6	2	4
Absolute	$AE	3	4
Absolute,Y	$BE	3	4 (+1 if page crossed)
			
"""


class Test_LDXInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    def test_LDXwithImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Check and see if NF is getting set correctly on a negative value
        # ZF should not change
        instructions = ([0xFFFC, 0xA2], [0xFFFD, 0x82])
        self.programSetup(instructions)
        self.processor.LDX_Immediate(2)
        self.assertEqual(
            self.processor.X, 0x82, "1 - LDXwithImmediate failed to load A correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Check and see if NF is not chaning on a positive load
        # ZF does not change.
        instructions = ([0xFFFC, 0xA2], [0xFFFD, 0x32])
        self.programSetup(instructions)
        self.processor.LDX_Immediate(2)
        self.assertEqual(
            self.processor.X, 0x32, "2 - LDXwithImmediate failed to load A correctly"
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
            self.processor.X, 0x82, "1 - LDXwithZeroPage failed to load x correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xA6], [0xFFFD, 0x00], [0x0000, 0x32])
        self.programSetup(instructions)
        self.processor.LDX_ZeroPage(3)
        self.assertEqual(
            self.processor.X, 0x32, "2 - LDXwithZeroPage failed to load x correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 2 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xA6], [0xFFFD, 0x00], [0x0000, 0x00])
        self.programSetup(instructions)
        self.processor.LDX_ZeroPage(3)
        self.assertEqual(
            self.processor.X, 0x00, "2 - LDXwithZeroPage failed to load X correctly"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        print("Complete: test_LDXwithZeroPage =======")
        del CPUCopy

    def test_LDXwithZeroPageY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Load from mem loc 0x10 Must be between 0x00 and 0xFF
        # For the locaion the MSB is always 0x00
        # For 0x82 - ZF should not change and NF get set
        instructions = ([0xFFFC, 0xA6], [0xFFFD, 0x00], [0x0010, 0x82])
        self.programSetup(instructions)
        self.processor.Y = 0x10  # Has to come after programSetup as that will reset proc and clear registers
        self.processor.LDX_ZeroPageWithY(3)
        self.assertEqual(
            self.processor.X,
            0x82,
            "1 - LDXwithZeroPageWithY failed to load Y correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xA6], [0xFFFD, 0x00], [0x0010, 0x32])
        self.programSetup(instructions)
        self.processor.Y = 0x10  # Has to come after programSetup as that will reset proc and clear registers
        self.processor.LDX_ZeroPageWithY(3)
        self.assertEqual(
            self.processor.X,
            0x32,
            "2 - LDXwithZeroPageWithY failed to load Y correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 2 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xA6], [0xFFFD, 0x00], [0x0010, 0x00])
        self.programSetup(instructions)
        self.processor.Y = 0x10  # Has to come after programSetup as that will reset proc and clear registers
        self.processor.LDX_ZeroPageWithY(3)
        self.assertEqual(
            self.processor.X,
            0x00,
            "2 - LDXwithZeroPageWithY failed to load Y correctly",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        print("Complete: test_LDXwithZeroPageWithY =======")
        del CPUCopy

    def test_LDXwithAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Instruction contains the full 16 bit address to the identify the target location
        instructions = ([0xFFFC, 0xAE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x4480, 0x82])
        self.programSetup(instructions)
        self.processor.LDX_Absolute(3)
        self.assertEqual(
            self.processor.X, 0x82, "1 - LDXwithAbsolute failed to load X correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xAE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x4480, 0x32])
        self.programSetup(instructions)
        self.processor.LDX_Absolute(3)
        self.assertEqual(
            self.processor.X, 0x32, "2 - LDXwithAbsolute failed to load X correctly"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 2 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xAE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x4480, 0x00])
        self.programSetup(instructions)
        self.processor.LDX_Absolute(3)
        self.assertEqual(
            self.processor.X, 0x00, "2 - LDXWithAbsolute failed to load X correctly"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        print("Complete: test_LDXwithAbsolute =======")
        del CPUCopy

    def test_LDXAbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        instructions = ([0xFFFC, 0xBE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x82])
        self.programSetup(instructions)
        self.processor.Y = 0x0F
        self.processor.LDX_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.X, 0x82, "1 - LDXAbsoluteWithY failed to load X"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xBE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x32])
        self.programSetup(instructions)
        self.processor.Y = 0x0F
        self.processor.LDX_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.X, 0x32, "2 - LDXAbsoluteWithY failed to load X"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 3 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xBE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x00])
        self.programSetup(instructions)
        self.processor.Y = 0x0F
        self.processor.LDX_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.X, 0x00, "2 - LDXAbsoluteWithY failed to load X"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # TODO: need to deal with wrapping at top end.

        print("Complete: LDXAbsoluteWithY=======")
        del CPUCopy
