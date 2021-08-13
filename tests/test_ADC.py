from architecture.processor import CPU_6502
import copy
import _BaseTest


class Test_ADCInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """
ADC - Add with Carry			
			
A,Z,C,N = A+M+C			
			
This instruction adds the contents of a memory location to the accumulator together with the carry bit. If overflow occurs the carry bit is set, this enables multiple byte addition to be performed.			
			
Processor Status after use:			
			
C	Carry Flag	Set if overflow in bit 7	
Z	Zero Flag	Set if A = 0	
I	Interrupt Disable	Not affected	
D	Decimal Mode Flag	Not affected	
B	Break Command	Not affected	
V	Overflow Flag	Set if sign bit is incorrect	
N	Negative Flag	Set if bit 7 set	
			
Addressing Mode	Opcode	Bytes	Cycles
Immediate	$69	2	2
Zero Page	$65	2	3
Zero Page,X	$75	2	4
Absolute	$6D	3	4
Absolute,X	$7D	3	4 (+1 if page crossed)
Absolute,Y	$79	3	4 (+1 if page crossed)
(Indirect,X)	$61	2	6
(Indirect),Y	$71	2	5 (+1 if page crossed)
"""

    def test_ADCImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x69], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ADC_Immediate(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "1 - ADCImmediate failed",
        )
        # 0xAA + 0xAA = 0x154
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 1 as the result is > 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x154 & 0xFF = 0x54, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 1, 1)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x69], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ADC_Immediate(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "2 - ADCImmediate failed",
        )
        # 0xAA + 0x00 = 0xAA
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0xAA & 0xFF = 0xAA, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x69], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ADC_Immediate(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "3 - ADCImmediate failed",
        )
        # 0x4A + 0x40 = 0x8A
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x8A & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_ADCImmediate=======")
        del CPUCopy

    def test_ADCZeroPage(self):
        CPUCopy = copy.deepcopy(self.processor)

        # For comparison at the end to ensure not inadvertent register flags changed
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x65], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ADC_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "1 - ADCZeroPage failed",
        )
        # 0xAA + 0xAA = 0x154
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 1 as the result is > 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x154 & 0xFF = 0x54, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 1, 1)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x65], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ADC_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "2 - ADCZeroPage failed",
        )
        # 0xAA + 0x00 = 0xAA
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0xAA & 0xFF = 0xAA, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x65], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.ADC_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "3 - ADCZeroPage failed",
        )
        # 0x4A + 0x40 = 0x8A
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x8A & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_ADCZeroPage =======")
        del CPUCopy

    def test_ADCZeroPageWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x75], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg
        self.processor.ADC_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "1 - ADCZeroPageWithX failed",
        )
        # 0xAA + 0xAA = 0x154
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 1 as the result is > 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x154 & 0xFF = 0x54, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 1, 1)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x75], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg
        self.processor.ADC_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "2 - ADCZeroPageWithX failed",
        )
        # 0xAA + 0x00 = 0xAA
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0xAA & 0xFF = 0xAA, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x75], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.ADC_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "3 - ADCZeroPageWithX failed",
        )
        # 0x4A + 0x40 = 0x8A
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x8A & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_ADCZeroPageWithX =======")
        del CPUCopy

    def test_ADCAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x6D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.ADC_Absolute(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "1 - ADCAbsolute failed",
        )
        # 0xAA + 0xAA = 0x154
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 1 as the result is > 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x154 & 0xFF = 0x54, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 1, 1)

        # Test 2 - Negative load
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
        self.processor.ADC_Absolute(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "2 - ADCAbsolute failed",
        )
        # 0xAA + 0x00 = 0xAA
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0xAA & 0xFF = 0xAA, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x6D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.ADC_Absolute(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "3 - ADCAbsolutefailed",
        )
        # 0x4A + 0x40 = 0x8A
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x8A & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_ADCAbsolute =======")
        del CPUCopy

    def test_ADCAbsoluteWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x7D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.X = 0x10
        self.processor.ADC_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "1 - ADCAbsoluteWithX failed",
        )
        # 0xAA + 0xAA = 0x154
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 1 as the result is > 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x154 & 0xFF = 0x54, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 1, 1)

        # Test 2 - Negative load
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
        self.processor.X = 0x10
        self.processor.ADC_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "2 - ADCAbsoluteWithX failed",
        )
        # 0xAA + 0x00 = 0xAA
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0xAA & 0xFF = 0xAA, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x7D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.X = 0x10
        self.processor.ADC_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "3 - ADCAbsoluteWithX failed",
        )
        # 0x4A + 0x40 = 0x8A
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x8A & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_ADCAbsoluteWithX =======")
        del CPUCopy

    def test_ADCAbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x79],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.Y = 0x10
        self.processor.ADC_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "1 - ADCAbsoluteWithY failed",
        )
        # 0xAA + 0xAA = 0x154
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 1 as the result is > 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x154 & 0xFF = 0x54, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 1, 1)

        # Test 2 - Negative load
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
        self.processor.Y = 0x10
        self.processor.ADC_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "2 - ADCAbsoluteWithY failed",
        )
        # 0xAA + 0x00 = 0xAA
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0xAA & 0xFF = 0xAA, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x79],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.Y = 0x10
        self.processor.ADC_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "3 - ADCAbsoluteWithY failed",
        )
        # 0x4A + 0x40 = 0x8A
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x8A & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_ADCAbsoluteWithY =======")
        del CPUCopy

    def test_ADCIndirectWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
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
        self.processor.X = 0x04
        self.processor.ADC_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "1 - ADCIndirectWithX failed",
        )
        # 0xAA + 0xAA = 0x154
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 1 as the result is > 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x154 & 0xFF = 0x54, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 1, 1)

        # Test 2 - Negative load
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
        self.processor.X = 0x04
        self.processor.ADC_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "2 - ADCIndirectWithX failed",
        )
        # 0xAA + 0x00 = 0xAA
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0xAA & 0xFF = 0xAA, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3
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
        self.processor.X = 0x04
        self.processor.ADC_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "3 - ADCIndirectWithX failed",
        )
        # 0x4A + 0x40 = 0x8A
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x8A & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_ADCIndirectWithX =======")
        del CPUCopy

    def test_ADCIndirectWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
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
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.ADC_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "1 - ADCIndirectWithY failed",
        )
        # 0xAA + 0xAA = 0x154
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 1 as the result is > 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x154 & 0xFF = 0x54, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 1, 1)

        # Test 2 - Negative load
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
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.ADC_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "2 - ADCIndirectWithY failed",
        )
        # 0xAA + 0x00 = 0xAA
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0xAA & 0xFF = 0xAA, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        # Test 3
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
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.ADC_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            (test_value_reg + test_value_mem) & 0x00FF,
            "3 - ADCIndirectWithY failed",
        )
        # 0x4A + 0x40 = 0x8A
        # expected result:
        # ZF = 0 as the result is not zero
        # CF = 0 as the result is < 0xFF
        # OF = 1 as the result is > 127
        # NF = 1 as 0x8A & 0xFF = 0x8A, which has bit 7 set.
        self.checkRegisters(CPUCopy, 0, 1, 0, 1)

        print("Complete: test_ADC_IndirectWithY =======")
        del CPUCopy
