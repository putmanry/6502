from architecture.processor import CPU_6502
import copy
import _BaseTest


class Test_TransferAccInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """
    TAX - Transfer Accumulator to X			
                
    X = A			
                
    Copies the current contents of the accumulator into the X register and sets
    the zero and negative flags as appropriate.			
                
    Processor Status after use:			
                
    C	Carry Flag	Not affected	
    Z	Zero Flag	Set if X = 0	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break Command	Not affected	
    V	Overflow Flag	Not affected	
    N	Negative Flag	Set if bit 7 of X is set	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Implied	$AA	1	2
                
    """

    def test_TAX(self):
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

    """
    TAY - Transfer Accumulator to Y			
			
    Y = A			
                
    Copies the current contents of the accumulator into the Y register and sets the zero and negative flags as appropriate.			
                
    Processor Status after use:			
                
    C	Carry Flag	Not affected	
    Z	Zero Flag	Set if Y = 0	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break Command	Not affected	
    V	Overflow Flag	Not affected	
    N	Negative Flag	Set if bit 7 of Y is set	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Implied	$A8	1	2
			
    """

    def test_TAY(self):
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

    """
    TXA - Transfer X to Accumulator			
			
    A = X			
                
    Copies the current contents of the X register into the accumulator and sets the zero and negative flags as appropriate.			
                
    Processor Status after use:			
                
    C	Carry Flag	Not affected	
    Z	Zero Flag	Set if A = 0	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break Command	Not affected	
    V	Overflow Flag	Not affected	
    N	Negative Flag	Set if bit 7 of A is set	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Implied	$8A	1	2
	"""

    def test_TXA(self):
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

    """
    TYA - Transfer Y to Accumulator			
			
    A = Y			
                
    Copies the current contents of the Y register into the accumulator and sets the zero and negative flags as appropriate.			
                
    Processor Status after use:			
                
    C	Carry Flag	Not affected	
    Z	Zero Flag	Set if A = 0	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break Command	Not affected	
    V	Overflow Flag	Not affected	
    N	Negative Flag	Set if bit 7 of A is set	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Implied	$98	1	2
    """

    def test_TYA(self):
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
