# Standard libarary imports
import copy
import datetime
import unittest

# local application imports
import _BaseTest
import processor

"""
LDA - Load Accumulator

A,Z,N = M			
			
Loads a byte of memory into the accumulator setting the zero and negative flags as appropriate.			
			
C	Carry Flag	Not affected	
Z	Zero Flag	Set if A = 0	
I	Interrupt Disable	Not affected	
D	Decimal Mode Flag	Not affected	
B	Break Command	Not affected	
V	Overflow Flag	Not affected	
N	Negative Flag	Set if bit 7 of A is set	
			
Addressing Mode	Opcode	Bytes	Cycles
Immediate	$A9	2	2
Zero Page	$A5	2	3
Zero Page,X	$B5	2	4
Absolute	$AD	3	4
Absolute,X	$BD	3	4 (+1 if page crossed)
Absolute,Y	$B9	3	4 (+1 if page crossed)
(Indirect,X)	$A1	2	6
(Indirect),Y	$B1	2	5 (+1 if page crossed)
			
"""


class Test_LDAInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    def test_LDAwithImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)
        cpu = CPU_6502

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

    def test_LDAZeroPageWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Load from mem loc 0x10 Must be between 0x00 and 0xFF
        # If X contains 0x0F and the ins is LDA $80,X then A is loaded
        #    from 0x008F (0x80 + 0x0F)
        # For 0x82 - ZF should not change and NF get set
        instructions = ([0xFFFC, 0xB5], [0xFFFD, 0x80], [0x008F, 0x82])
        self.programSetup(instructions)
        self.processor.X = 0x0F
        self.processor.LDA_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDAwithZeroPageWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xB5], [0xFFFD, 0x80], [0x008F, 0x32])
        self.programSetup(instructions)
        self.processor.X = 0x0F
        self.processor.LDA_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDAwithZeroPageWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 3 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xB5], [0xFFFD, 0x80], [0x008F, 0x00])
        self.programSetup(instructions)
        self.processor.X = 0x0F
        self.processor.LDA_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A, 0x00, "2 - LDAwithZeroPageWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # TODO: need to deal with wrapping at top end.

        print("Complete: test_LDAwithZeroPageWithX =======")
        del CPUCopy

    def test_LDAAbsoluteWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # If X containes 0x92 and we have an LDA 0x2000, X the instruction will load from
        # 0x2092.
        instructions = ([0xFFFC, 0xAD], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x82])
        self.programSetup(instructions)
        self.processor.X = 0x0F
        self.processor.LDA_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDAAbsoluteWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xAD], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x32])
        self.programSetup(instructions)
        self.processor.X = 0x0F
        self.processor.LDA_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDAAbsoluteWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 3 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xAD], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x00])
        self.programSetup(instructions)
        self.processor.X = 0x0F
        self.processor.LDA_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A, 0x00, "2 - LDAAbsoluteWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # TODO: need to deal boundary crossing.
        # if the addition of the X byte causes the lo byte to overflow
        # into the upper byte that adds an extra cycle.

        print("Complete: LDAAbsoluteWithX =======")
        del CPUCopy

    def test_LDAwithAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Instruction contains the full 16 bit address to the identify the target location
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

    def test_LDAAbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # If X containes 0x92 and we have an LDA 0x2000, X the instruction will load from
        # 0x2092.
        instructions = ([0xFFFC, 0xAD], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x82])
        self.programSetup(instructions)
        self.processor.Y = 0x0F
        self.processor.LDA_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDAAbsoluteWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xAD], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x32])
        self.programSetup(instructions)
        self.processor.Y = 0x0F
        self.processor.LDA_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDAAbsoluteWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 3 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xAD], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x00])
        self.programSetup(instructions)
        self.processor.Y = 0x0F
        self.processor.LDA_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A, 0x00, "2 - LDAAbsoluteWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # TODO: need to deal with wrapping at top end.

        print("Complete: LDAAbsoluteWithY=======")
        del CPUCopy

    def test_LDAIndirectWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # If X containes 0x92 and we have an LDA 0x2000, X the instruction will load from
        # 0x2092.
        instructions = (
            [0xFFFC, 0xA1],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, 0x82],
        )
        self.programSetup(instructions)
        self.processor.X = 0x04
        self.processor.LDA_IndirectWithX(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDAIndirectWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = (
            [0xFFFC, 0xA1],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, 0x32],
        )
        self.programSetup(instructions)
        self.processor.X = 0x04
        self.processor.LDA_IndirectWithX(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDAIndirectWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 3 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = (
            [0xFFFC, 0xA1],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, 0x00],
        )
        self.programSetup(instructions)
        self.processor.X = 0x04
        self.processor.LDA_IndirectWithX(3)
        self.assertEqual(
            self.processor.A, 0x00, "3 - LDAIndirectWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 4 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = (
            [0xFFFC, 0xA1],
            [0xFFFD, 0x20],
            [0x0024, 0x74],
            [0x0025, 0x20],
            [0x2074, 0x82],
        )
        self.programSetup(instructions)
        self.processor.X = 0x04
        self.processor.LDA_IndirectWithX(3)
        self.assertEqual(
            self.processor.A, 0x82, "4 - LDAIndirectWithX failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        print("Complete: LDAIndirectWithX =======")
        del CPUCopy

    def test_LDAIndirectWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # test 0 -
        # The operand xx is a zero page address, the contents of xx are added with carry (C)
        # to the Y register
        #      xx + Y (C) the results containts the LSB of the EA
        # The content of address $AA + $01 + C contain the MSB of the EA
        # if Y = $E9 and
        # if $A4 contains $51 and
        # if $A5 contains $3F then:
        # LDA ($A4), Y results in
        # $A4 + Y (C) => ($51 + $E9) (C) => $13A (C) => $3A -> EA LSB and
        # $A4 + $01 (C) -> ($3F + C) => ($3F + $01) => $40 -> EA MSB
        #                                                   $403A EA

        instructions = (
            [0xFFFC, 0xB1],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, 0x82],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.LDA_IndirectWithY(3)
        self.assertEqual(
            self.processor.A, 0x82, "0 - LDAIndirectWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)
        # Test 1 -
        instructions = (
            [0xFFFC, 0xB1],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, 0x82],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.LDA_IndirectWithY(3)
        self.assertEqual(
            self.processor.A, 0x82, "1 - LDAIndirectWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = (
            [0xFFFC, 0xB1],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, 0x32],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.LDA_IndirectWithY(3)
        self.assertEqual(
            self.processor.A, 0x32, "2 - LDAIndirectWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 3 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = (
            [0xFFFC, 0xB1],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, 0x00],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.LDA_IndirectWithY(3)
        self.assertEqual(
            self.processor.A, 0x00, "3 - LDAIndirectWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 4 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = (
            [0xFFFC, 0xB1],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, 0x82],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.LDA_IndirectWithY(3)
        self.assertEqual(
            self.processor.A, 0x82, "4 - LDAIndirectWithY failed to load A"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        print("Complete: LDAIndirectWithY =======")
        del CPUCopy
