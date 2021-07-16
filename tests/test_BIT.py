from architecture.processor import CPU_6502
import copy
import _BaseTest


class test_BITInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """
    BIT - Bit Test			
			
    A & M, N = M7, V = M6			
                
    This instructions is used to test if one or more bits are set in a target 
    memory location. The mask pattern in A is ANDed with the value in memory 
    to set or clear the zero flag, but the result is not kept. Bits 7 and 6 of the 
    value from memory are copied into the N and V flags.			
                
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

        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x24], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.BIT_ZeroPage(3)
        self.assertEqual(self.processor.NF, 1, "1A - BITZero NF incorrect")
        self.assertEqual(self.processor.OF, 0, "1B - BITZero OF incorrect")

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x24], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.BIT_ZeroPage(3)
        self.assertEqual(self.processor.NF, 1, "2A - BITZero NF incorrect")
        self.assertEqual(self.processor.OF, 0, "2B - BITZero OF incorrect")
        self.assertEqual(self.processor.ZF, 0, "2B - BITZero ZF incorrect")

        # Test 3
        test_value_mem = 0xC0
        test_value_reg = 0xC0
        instructions = ([0xFFFC, 0x24], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.BIT_ZeroPage(3)
        self.assertEqual(self.processor.NF, 1, "3A - BITZero NF incorrect")
        self.assertEqual(self.processor.OF, 1, "3B - BITZero OF incorrect")

        print("Complete: test_BITZeroPage =======")

    def test_BITAbsolute(self):
        # Test 1 - Zero load
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x24],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x4480, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.BIT_Absolute(3)
        self.assertEqual(self.processor.NF, 1, "1A - BITZero NF incorrect")
        self.assertEqual(self.processor.OF, 0, "1B - BITZero OF incorrect")

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x24],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x4480, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.BIT_Absolute(3)
        self.assertEqual(self.processor.NF, 1, "2A - BITZero NF incorrect")
        self.assertEqual(self.processor.OF, 0, "2B - BITZero OF incorrect")
        self.assertEqual(self.processor.ZF, 0, "2B - BITZero ZF incorrect")

        # Test 3
        test_value_mem = 0xC0
        test_value_reg = 0xC0
        instructions = (
            [0xFFFC, 0x24],
            [0xFFFD, 0x80],
            [0xFFFE, 0x44],
            [0x4480, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.BIT_Absolute(3)
        self.assertEqual(self.processor.NF, 1, "3A - BITZero NF incorrect")
        self.assertEqual(self.processor.OF, 1, "3B - BITZero OF incorrect")

        print("Complete: test_BITAbsolute =======")
