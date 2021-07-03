from architecture.processor import CPU_6502
import copy
import _BaseTest


class test_BITInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """
    BIT - Bit Test			
			
    A & M, N = M7, V = M6			
                
    This instructions is used to test if one or more bits are set in a target memory location. The mask pattern in A is ANDed with the value in memory to set or clear the zero flag, but the result is not kept. Bits 7 and 6 of the value from memory are copied into the N and V flags.			
                
    Processor Status after use:			
                
    C	Carry Flag	Not affected	
    Z	Zero Flag	Set if the result if the AND is zero	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break Command	Not affected	
    V	Overflow Flag	Set to bit 6 of the memory value	
    N	Negative Flag	Set to bit 7 of the memory value	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Zero Page	$24	2	3
    Absolute	$2C	3	4
                
    """

    def test_BITZeroPage(self):
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

    def test_BITAbsolute(self):
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
