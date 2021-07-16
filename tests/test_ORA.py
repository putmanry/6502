from architecture.processor import CPU_6502
import copy
import _BaseTest


class Test_ORAInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """
   ORA - Logical Inclusive OR			
			
    A,Z,N = A|M			
                
    An inclusive OR is performed, bit by bit, on the accumulator contents using the contents of a byte of memory.			
                
    Processor Status after use:			
                
    C	Carry Flag	Not affected	
    Z	Zero Flag	Set if A = 0	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break CommORA	Not affected	
    V	Overflow Flag	Not affected	
    N	Negative Flag	Set if bit 7 set	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Immediate	$9	2	2
    Zero Page	$5	2	3
    Zero Page,X	$15	2	4
    Absolute	$0D	3	4
    Absolute,X	$1D	3	4 (+1 if page crossed)
    Absolute,Y	$19	3	4 (+1 if page crossed)
    (Indirect,X)	$1	2	6
    (Indirect),Y	$11	2	5 (+1 if page crossed
			
                
    """

    def test_ORAImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x09], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ORA_Immediate(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "1 - ORAImmediate failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x09], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ORA_Immediate(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "2 - ORAImmediate failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3 - Positive load
        test_value_mem = 0x30
        test_value_reg = 0x20
        instructions = ([0xFFFC, 0x09], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ORA_Immediate(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "3 - ORAImmediate failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_ORAImmediate=======")
        del CPUCopy

    def test_ORAZeroPage(self):
        CPUCopy = copy.deepcopy(self.processor)

        # For comparison at the end to ensure not inadvertent register flags changed
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ORA_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "1 - ORAZeroPage failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ORA_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "2 - ORAZeroPage failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3
        test_value_mem = 0x30
        test_value_reg = 0x20
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.ORA_ZeroPage(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "3 - ORAZeroPage failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_ORAZeroPage =======")
        del CPUCopy

    def test_ORAZeroPageWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x15], [0xFFFD, 0x80], [0x008F, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x0F
        self.processor.A = test_value_reg
        self.processor.ORA_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "1 - ORAZeroPageWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x15], [0xFFFD, 0x80], [0x008F, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x0F
        self.processor.A = test_value_reg
        self.processor.ORA_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "2 - ORAZeroPageWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3
        test_value_mem = 0x30
        test_value_reg = 0x20
        instructions = ([0xFFFC, 0x15], [0xFFFD, 0x80], [0x008F, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x0F
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.ORA_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "3 - ORAZeroPageWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_ORAZeroPageWithX =======")
        del CPUCopy

    def test_ORAAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x0D],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x4480, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.ORA_Absolute(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "1 - ORAAbsolute failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x0D],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x4480, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.ORA_Absolute(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "2 - ORAAbsolute failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3
        test_value_mem = 0x30
        test_value_reg = 0x20
        instructions = (
            [0xFFFC, 0x0D],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x4480, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.ORA_Absolute(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "3 - ORAAbsolutefailed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_ORAAbsolute =======")
        del CPUCopy

    def test_ORAAbsoluteWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x1D],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x448F, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.X = 0x0F
        self.processor.ORA_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "1 - ORAAbsoluteWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x1D],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x448F, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x0F
        self.processor.ORA_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "2 - ORAAbsoluteWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3
        test_value_mem = 0x30
        test_value_reg = 0x20
        instructions = (
            [0xFFFC, 0x1D],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x448F, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x0F
        self.processor.ORA_AbsoluteWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "3 - ORAAbsoluteWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_ORAAbsoluteWithX =======")
        del CPUCopy

    def test_ORAAbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x1D],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x448F, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.Y = 0x0F
        self.processor.ORA_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "1 - ORAAbsoluteWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x1D],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x448F, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.Y = 0x0F
        self.processor.ORA_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "2 - ORAAbsoluteWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3
        test_value_mem = 0x30
        test_value_reg = 0x20
        instructions = (
            [0xFFFC, 0x1D],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x448F, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.Y = 0x0F
        self.processor.ORA_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "3 - ORAAbsoluteWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_ORAAbsoluteWithY =======")
        del CPUCopy

    def test_ORAIndirectWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0x4A
        test_value_reg = 0x40
        instructions = (
            [0xFFFC, 0x01],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x04
        self.processor.ORA_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "1 - ORAIndirectWithX failed",
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
        self.processor.ORA_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "2 - ORAIndirectWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3
        test_value_mem = 0x30
        test_value_reg = 0x20
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
        self.processor.ORA_IndirectWithX(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "3 - ORAIndirectWithX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_ORAIndirectWithX =======")
        del CPUCopy

    def test_ORAIndirectWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x11],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.ORA_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "1 - ORAIndirectWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 - Negative load
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x11],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.ORA_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "2 - ORAIndirectWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3
        test_value_mem = 0x30
        test_value_reg = 0x20
        instructions = (
            [0xFFFC, 0x11],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.ORA_IndirectWithY(3)
        self.assertEqual(
            self.processor.A,
            test_value_reg | test_value_mem,
            "3 - ORAIndirectWithY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_ORA_IndirectWithY =======")
        del CPUCopy
