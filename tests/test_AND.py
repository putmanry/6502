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

        # Test 1 - Zero load
        instructions = ([0xFFFC, 0xAA], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.A = 0x00  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TAX(3)
        self.assertEqual(
            self.processor.A,
            self.processor.X,
            "1 - TAX failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2 - Negative load
        instructions = ([0xFFFC, 0xAA], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.A = 0x8F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TAX(3)
        self.assertEqual(
            self.processor.A,
            self.processor.X,
            "2 - TAX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3 - Positive load
        instructions = ([0xFFFC, 0xAA], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.A = 0x7F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TAX(3)
        self.assertEqual(
            self.processor.A,
            self.processor.X,
            "3 - TAX failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_TAX =======")
        del CPUCopy

    def test_ANDZeroPage(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        instructions = ([0xFFFC, 0xA8], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x00  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TAY(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "1 - TAY failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2 - Negative load
        instructions = ([0xFFFC, 0xA8], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x8F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TAY(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "2 - TAY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3 - Positive load
        instructions = ([0xFFFC, 0xA8], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x7F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TAY(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "3 - TAY failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_TAY =======")
        del CPUCopy

    def test_ANDZeroPageWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        instructions = ([0xFFFC, 0x8A], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.X = 0x00  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TXA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.X,
            "1 - TXA failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2 - Negative load
        instructions = ([0xFFFC, 0x8A], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.X = 0x8F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TXA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.X,
            "2 - TXA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3 - Positive load
        instructions = ([0xFFFC, 0x8A], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.X = 0x7F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TXA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.X,
            "3 - TXA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_TXA =======")
        del CPUCopy

    def test_ANDAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x00  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "1 - TYA failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2 - Negative load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x8F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "2 - TYA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3 - Positive load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x7F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "3 - TYA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_TYA =======")
        del CPUCopy

    def test_ANDAbsoluteWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x00  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "1 - TYA failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2 - Negative load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x8F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "2 - TYA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3 - Positive load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x7F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "3 - TYA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_TYA =======")
        del CPUCopy

    def test_ANDAbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x00  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "1 - TYA failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2 - Negative load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x8F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "2 - TYA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3 - Positive load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x7F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "3 - TYA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_TYA =======")
        del CPUCopy

    def test_ANDIndirectWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x00  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "1 - TYA failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2 - Negative load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x8F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "2 - TYA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3 - Positive load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x7F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "3 - TYA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_TYA =======")
        del CPUCopy

    def test_ANDIndirectWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 - Zero load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x00  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "1 - TYA failed",
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # Test 2 - Negative load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x8F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "2 - TYA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 3 - Positive load
        instructions = ([0xFFFC, 0x98], [0xFFFD, 0xBB])
        self.programSetup(instructions)
        self.processor.Y = 0x7F  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.TYA(3)
        self.assertEqual(
            self.processor.A,
            self.processor.Y,
            "3 - TYA failed",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 0)

        print("Complete: test_TYA =======")
        del CPUCopy
