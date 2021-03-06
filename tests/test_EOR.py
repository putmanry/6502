from architecture.processor import CPU_6502
import copy
import _BaseTest


class Test_EORInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """
   EOR - Exclusive OR			
			
    A,Z,N = A^M			
                
    An exclusive OR is performed, bit by bit, on the accumulator contents using the contents of a byte of memory.			
                
    Processor Status after use:			
                
    C	Carry Flag	Not affected	
    Z	Zero Flag	Set if A = 0	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break Command	Not affected	
    V	Overflow Flag	Not affected	
    N	Negative Flag	Set if bit 7 set	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Immediate	$49	2	2
    Zero Page	$45	2	3
    Zero Page,X	$55	2	4
    Absolute	$4D	3	4
    Absolute,X	$5D	3	4 (+1 if page crossed)
    Absolute,Y	$59	3	4 (+1 if page crossed)
    (Indirect,X)	$41	2	6
    (Indirect),Y	$51	2	5 (+1 if page crossed)
                
                
    """

    def test_EORImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x29], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.EOR_Immediate(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "1 - EORImediate failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x29], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.EOR_Immediate(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "2 - EORImmediate failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3 - Positive load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x29], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.EOR_Immediate(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "3 - EORImmediate failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_EORImmediate=======")
        del CPUCopy

    def test_EORZeroPage(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.EOR_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "1 - EORZeroPage failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.EOR_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "2 - EORZeroPage failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.EOR_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "3 - EORZeroPage failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_EORZeroPage =======")
        del CPUCopy

    def test_EORZeroPageWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x35], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg
        self.processor.EOR_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "1 - test_EORZeroPageWithX failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x35], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg
        self.processor.EOR_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "2 - test_EORZeroPageWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = ([0xFFFC, 0x35], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.EOR_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "3 - test_EORZeroPageWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_EORZeroPageWithX =======")
        del CPUCopy

    def test_EORAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.EOR_Absolute(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "1 - test_EORAbsolute failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

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
        self.processor.EOR_Absolute(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "2 - test_EORAbsolute failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

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
        self.processor.EOR_Absolute(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "3 - test_EORAbsolute",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_EORAbsolute =======")
        del CPUCopy

    def test_EORAbsoluteWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x3D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.X = 0x10
        self.processor.EOR_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "1 - test_EORAbsoluteWithX failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

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
        self.processor.EOR_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "2 - test_EORAbsoluteWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

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
        self.processor.EOR_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "3 - test_EORAbsoluteWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_EORAbsoluteWithXt_TYA =======")
        del CPUCopy

    def test_EORAbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x39],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.Y = 0x10
        self.processor.EOR_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "1 - test_EORAbsoluteWithY failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

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
        self.processor.EOR_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "2 - test_EORAbsoluteWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

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
        self.processor.EOR_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "3 - test_EORAbsoluteWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_EORAbsoluteWithY =======")
        del CPUCopy

    def test_EORIndirectWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
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
        self.processor.EOR_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "1 - test_EORIndirectWithX failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

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
        self.processor.EOR_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "2 - test_EORIndirectWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

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
        self.processor.EOR_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "3 - test_EORIndirectWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_EORIndirectWithX =======")
        del CPUCopy

    def test_EORIndirectWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
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
        self.processor.EOR_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "1 - test_EORIndirectWithY failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

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
        self.processor.EOR_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "2 - test_EORIndirectWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

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
        self.processor.EOR_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg ^ test_value_mem,
            "3 - test_EORIndirectWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_EORIndirectWithY =======")
        del CPUCopy
