from architecture.processor import CPU_6502
import copy
import _BaseTest


class Test_ANDInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """
   AND - Logical AND			
			
    A,Z,N = A&M			
                
    A logical AND is performed, bit by bit, on the accumulator contents using the contents of a byte of memory.			
                
    Processor Status after use:			
                
    C	Carry Flag	Not affected	
    Z	Zero Flag	Set if A = 0	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break Command	Not affected	
    V	Overflow Flag	Not affected	
    N	Negative Flag	Set if bit 7 set	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Immediate	$29	2	2
    Zero Page	$25	2	3
    Zero Page,X	$35	2	4
    Absolute	$2D	3	4
    Absolute,X	$3D	3	4 (+1 if page crossed)
    Absolute,Y	$39	3	4 (+1 if page crossed)
    (Indirect,X)	$21	2	6
    (Indirect),Y	$31	2	5 (+1 if page crossed)
			
                
    """

    def test_ANDImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x29], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.AND_Immediate(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "1 - ANDImmediate failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x29], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.AND_Immediate(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "2 - ANDImmediate failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 3 - Positive load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x29], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.AND_Immediate(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "3 - ANDImmediate failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        print("Complete: test_ANDImmediate=======")
        del CPUCopy

    def test_ANDZeroPage(self):
        CPUCopy = copy.deepcopy(self.processor)

        # For comparison at the end to ensure not inadvertent register flags changed
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.AND_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "1 - ANDZeroPage failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.AND_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "2 - ANDZeroPage failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.AND_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "3 - ANDZeroPage failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        print("Complete: test_ANDZeroPage =======")
        del CPUCopy

    def test_ANDZeroPageWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x35], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg
        self.processor.AND_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "1 - ANDZeroPageWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x35], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg
        self.processor.AND_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "2 - ANDZeroPageWithX failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x35], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.AND_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "3 - ANDZeroPageWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        print("Complete: test_ANDZeroPageWithX =======")
        del CPUCopy

    def test_ANDAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.AND_Absolute(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "1 - ANDAbsolute failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.AND_Absolute(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "2 - ANDAbsolute failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.AND_Absolute(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "3 - ANDAbsolutefailed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        print("Complete: test_ANDAbsolute =======")
        del CPUCopy

    def test_ANDAbsoluteWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x3D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.X = 0x10
        self.processor.AND_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "1 - ANDAbsoluteWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x3D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x10
        self.processor.AND_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "2 - ANDAbsoluteWithX failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x3D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.X = 0x10
        self.processor.AND_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "3 - ANDAbsoluteWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        print("Complete: test_ANDAbsoluteWithX =======")
        del CPUCopy

    def test_ANDAbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x39],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.Y = 0x10
        self.processor.AND_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "1 - ANDAbsoluteWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x39],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.Y = 0x10
        self.processor.AND_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "2 - ANDAbsoluteWithY failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x39],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.Y = 0x10
        self.processor.AND_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "3 - ANDAbsoluteWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        print("Complete: test_ANDAbsoluteWithY =======")
        del CPUCopy

    def test_ANDIndirectWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x21],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x04
        self.processor.AND_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "1 - ANDIndirectWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x21],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x04
        self.processor.AND_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "2 - ANDIndirectWithX failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x21],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x04
        self.processor.AND_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "3 - ANDIndirectWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        print("Complete: test_ANDIndirectWithX =======")
        del CPUCopy

    def test_ANDIndirectWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x31],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.AND_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "1 - ANDIndirectWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x31],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.AND_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "2 - ANDIndirectWithY failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x31],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.AND_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg & test_value_mem,
            "3 - ANDIndirectWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        print("Complete: test_AND_IndirectWithY =======")
        del CPUCopy
