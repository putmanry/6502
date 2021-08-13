from architecture.processor import CPU_6502
import copy
import _BaseTest


class Test_SBCInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """
SBC - Subtract with Carry			
			
A,Z,C,N = A-M-(1-C)			
			
This instruction subtracts the contents of a memory location to the accumulator 
together with the not of the carry bit. If overflow occurs the carry bit is clear, 
this enables multiple byte subtraction to be performed.			
			
Processor Status after use:			
			
C	Carry Flag	Clear if overflow in bit 7	
Z	Zero Flag	Set if A = 0	
I	Interrupt Disable	Not affected	
D	Decimal Mode Flag	Not affected	
B	Break Command	Not affected	
V	Overflow Flag	Set if sign bit is incorrect	
N	Negative Flag	Set if bit 7 set	
			
Addressing Mode	Opcode	Bytes	Cycles
Immediate	$E9	2	2
Zero Page	$E5	2	3
Zero Page,X	$F5	2	4
Absolute	$ED	3	4
Absolute,X	$FD	3	4 (+1 if page crossed)
Absolute,Y	$F9	3	4 (+1 if page crossed)
(Indirect,X)	$E1	2	6
(Indirect),Y	$F1	2	5 (+1 if page crossed)
			
"""

    def test_SBCImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x69], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        # set the CF since not using two's complent add to do the subtraction
        self.processor.CF = 1
        self.processor.SBC_Immediate(3)
        self.assertEqual(
            self.processor.A,
            0,
            "1 - SBCImmediate failed",
        )
        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is < 0xFF
        # OF = 0 as the result is < 127 and > -128
        # NF =  as 0x00 & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x69], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.SBC_Immediate(3)
        self.assertEqual(
            self.processor.A,
            0x56,
            "2 - SBCImmediate failed",
        )
        # 0x00 - 0xAA = 0x56
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3 - Positive load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x69], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.SBC_Immediate(3)
        self.assertEqual(
            self.processor.A,
            0xF6,
            "3 - SBCImmediate failed",
        )
        # 0x40 - 0x4A = 0xF6
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_SBCImmediate=======")
        del CPUCopy

    def test_SBCZeroPage(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x65], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        # set the CF since not using two's complent add to do the subtraction
        self.processor.CF = 1
        self.processor.SBC_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            0,
            "1 - SBC_ZeroPage failed",
        )
        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is < 0xFF
        # OF = 0 as the result is < 127 and > -128
        # NF =  as 0x00 & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x65], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.SBC_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            0x56,
            "2 - SBC_ZeroPage failed",
        )
        # 0x00 - 0xAA = 0x56
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3 - Positive load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x65], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.SBC_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            0xF6,
            "3 - SBC_ZeroPage failed",
        )
        # 0x40 - 0x4A = 0xF6
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_SBC_ZeroPage=======")
        del CPUCopy

    def test_SBCZeroPageWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x75], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        # set the CF since not using two's complent add to do the subtraction
        self.processor.CF = 1
        self.processor.X = 0x10
        self.processor.SBC_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            0,
            "1 - SBC_ZeroPageWithX failed",
        )
        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is < 0xFF
        # OF = 0 as the result is < 127 and > -128
        # NF =  as 0x00 & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x75], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.X = 0x10
        self.processor.SBC_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            0x56,
            "2 - SBC_ZeroPageWithX failed",
        )
        # 0x00 - 0xAA = 0x56
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3 - Positive load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x75], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.X = 0x10
        self.processor.SBC_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            0xF6,
            "3 - SBC_ZeroPageWithX failed",
        )
        # 0x40 - 0x4A = 0xF6
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_SBC_ZeroPageWithX=======")
        del CPUCopy

    def test_SBCAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x6D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        # set the CF since not using two's complent add to do the subtraction
        self.processor.CF = 1
        self.processor.SBC_Absolute(3)
        self.assertEqual(
            self.processor.A,
            0,
            "1 - SBC_Absolute failed",
        )
        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is < 0xFF
        # OF = 0 as the result is < 127 and > -128
        # NF =  as 0x00 & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x6D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.SBC_Absolute(3)
        self.assertEqual(
            self.processor.A,
            0x56,
            "2 - SBC_Absolute failed",
        )
        # 0x00 - 0xAA = 0x56
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3 - Positive load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x6D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.SBC_Absolute(3)
        self.assertEqual(
            self.processor.A,
            0xF6,
            "3 - SBC_Absolute failed",
        )
        # 0x40 - 0x4A = 0xF6
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_SBC_Absolute=======")
        del CPUCopy

    def test_SBCAbsoluteWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x7D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        # set the CF since not using two's complent add to do the subtraction
        self.processor.CF = 1
        self.processor.X = 0x10
        self.processor.SBC_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            0,
            "1 - SBC_AbsoluteWithX failed",
        )
        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is < 0xFF
        # OF = 0 as the result is < 127 and > -128
        # NF =  as 0x00 & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x7D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.X = 0x10
        self.processor.SBC_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            0x56,
            "2 - SBC_AbsoluteWithX failed",
        )
        # 0x00 - 0xAA = 0x56
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3 - Positive load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x7D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.X = 0x10
        self.processor.SBC_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            0xF6,
            "3 - SBC_AbsoluteWithX failed",
        )
        # 0x40 - 0x4A = 0xF6
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_SBC_AbsoluteWithX=======")
        del CPUCopy

    def test_SBCAbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x79],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        # set the CF since not using two's complent add to do the subtraction
        self.processor.CF = 1
        self.processor.Y = 0x10
        self.processor.SBC_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            0,
            "1 - SBC_AbsoluteWithY failed",
        )
        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is < 0xFF
        # OF = 0 as the result is < 127 and > -128
        # NF =  as 0x00 & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x79],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.Y = 0x10
        self.processor.SBC_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            0x56,
            "2 - SBC_AbsoluteWithY failed",
        )
        # 0x00 - 0xAA = 0x56
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3 - Positive load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x79],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.Y = 0x10
        self.processor.SBC_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            0xF6,
            "3 - SBC_AbsoluteWithY failed",
        )
        # 0x40 - 0x4A = 0xF6
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_SBC_AbsoluteWithY=======")
        del CPUCopy

    def test_SBCIndirectWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x61],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        # set the CF since not using two's complent add to do the subtraction
        self.processor.CF = 1
        self.processor.X = 0x04
        self.processor.SBC_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            0,
            "1 - SBC_IndirectWithX failed",
        )
        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is < 0xFF
        # OF = 0 as the result is < 127 and > -128
        # NF =  as 0x00 & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x61],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.X = 0x04
        self.processor.SBC_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            0x56,
            "2 - SBC_IndirectWithX failed",
        )
        # 0x00 - 0xAA = 0x56
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3 - Positive load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x61],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.X = 0x04
        self.processor.SBC_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            0xF6,
            "3 - SBCImmediate failed",
        )
        # 0x40 - 0x4A = 0xF6
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_SBC_IndirectWithX=======")
        del CPUCopy

    def test_SBCIndirectWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x71],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        # set the CF since not using two's complent add to do the subtraction
        self.processor.CF = 1
        self.processor.Y = 0xE9
        self.processor.SBC_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            0,
            "1 - SBC_IndirectWithY failed",
        )
        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is < 0xFF
        # OF = 0 as the result is < 127 and > -128
        # NF =  as 0x00 & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x71],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.Y = 0xE9
        self.processor.SBC_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            0x56,
            "2 - SBC_IndirectWithY failed",
        )
        # 0x00 - 0xAA = 0x56
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3 - Positive load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x71],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CF = 1
        self.processor.Y = 0xE9
        self.processor.SBC_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            0xF6,
            "3 - SBC_IndirectWithY failed",
        )
        # 0x40 - 0x4A = 0xF6
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is < 127 and > -128
        # NF = 1 as result is negative
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_SBC_IndirectWithY=======")
        del CPUCopy
