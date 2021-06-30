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


def test_EORZeroPage(self):
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


def test_EORZeroPageWithX(self):
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


def test_EORAbsolute(self):
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


def test_EORAbsoluteWithX(self):
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


def test_EORAbsoluteWithY(self):
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


def test_EORIndirectWithX(self):
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


def test_EORIndirectWithY(self):
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
