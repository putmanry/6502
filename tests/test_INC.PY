from architecture.processor import CPU_6502
import copy
import _BaseTest


class Test_INCInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """

    INC - Increment Memory			
                
    M,Z,N = M+1			
                
    Adds one to the value held at a specified memory location setting the zero
    and negative flags as appropriate.			
                
    Processor Status after use:			
                
    C	Carry Flag	Not affected	
    Z	Zero Flag	Set if result is zero	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break Command	Not affected	
    V	Overflow Flag	Not affected	
    N	Negative Flag	Set if bit 7 of the result is set	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Zero Page	$E6	2	5
    Zero Page,X	$F6	2	6
    Absolute	$EE	3	6
    Absolute,X	$FE	3	7

"""

    def test_INCZeroPage(self):
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        zero_page_mem_addr = 0x10
        instructions = (
            [0xFFFC, 0xE6],
            [0xFFFD, zero_page_mem_addr],
            [zero_page_mem_addr, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.INC_ZeroPage(3)
        self.assertEqual(
            self.processor.memory[zero_page_mem_addr],
            test_value_mem + 1,
            "1 - INCZeroPage failed",
        )
        # 0xAA + 1 = 0xAB
        # expected result:
        # ZF = 0 as not
        # NF = 1 as the result is > 0x4F
        self.checkRegisters(CPUCopy, 0, 1, 0, 0)

        # Test 2
        test_value_mem = 0x00
        zero_page_mem_addr = 0x10
        instructions = (
            [0xFFFC, 0xE6],
            [0xFFFD, zero_page_mem_addr],
            [zero_page_mem_addr, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.INC_ZeroPage(3)
        self.assertEqual(
            self.processor.memory[zero_page_mem_addr],
            test_value_mem + 1,
            "2 - INCZeroPage failed",
        )
        # 0xAA + 1 = 0xAB
        # expected result:
        # ZF = 0 as not
        # NF = 0 as the result is < 0x4F
        self.checkRegisters(CPUCopy, 0, 0, 0, 0)

        # Test 3
        test_value_mem = 0xFF
        zero_page_mem_addr = 0x10
        instructions = (
            [0xFFFC, 0xE6],
            [0xFFFD, zero_page_mem_addr],
            [zero_page_mem_addr, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.INC_ZeroPage(3)
        # Have to remember that these are 8 bit values,
        # so make them if we have an overflow of something
        self.assertEqual(
            self.processor.memory[zero_page_mem_addr] & 0x00FF,
            (test_value_mem + 1) & 0x00FF,
            "3 - INCZeroPage failed",
        )
        # 0xAA + 1 = 0xAB
        # expected result:
        # ZF = 1 as it is.
        # NF = 0 as the result is < 0x4F
        self.checkRegisters(CPUCopy, 1, 0, 0, 0)

        print("Complete: test_INCZeroPage=======")
        del CPUCopy

    def test_INCZeroPageWithX(self):
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        instructions = ([0xFFFC, 0xF6], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.INC_ZeroPageWithX(3)

        # Mem + addr(reg) = mem + 1
        # expected result:
        # ZF = 0 as the result is not zero
        # NF = 1 as the value is >= 0x4F
        self.checkRegisters(CPUCopy, 0, 1, 0, 0)

        # Test 2
        test_value_mem = 0xFF
        instructions = ([0xFFFC, 0xF6], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.INC_ZeroPageWithX(3)

        # expected result:
        # ZF = 1 as the result is zero
        # NF = 0 as the value is <= 0x4F
        self.checkRegisters(CPUCopy, 1, 0, 0, 0)

        # Test 3
        test_value_mem = 0x40
        instructions = ([0xFFFC, 0xF6], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.INC_ZeroPageWithX(3)

        # expected result:
        # ZF = 0 as the result is not zero
        # NF = 0 as the value is <= 0x4F
        self.checkRegisters(CPUCopy, 0, 0, 0, 0)

        print("Complete: test_INCZeroPageWithX =======")
        del CPUCopy

    def test_INCAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        test_value_mem = 0xAA
        instructions = (
            [0xFFFC, 0xEE],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.INC_Absolute(3)

        # Mem + addr(reg) = mem + 1
        # expected result:
        # ZF = 0 as the result is not zero
        # NF = 1 as the value is >= 0x4F
        self.checkRegisters(CPUCopy, 0, 1, 0, 0)

        # Test 2
        test_value_mem = 0xFF
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.INC_Absolute(3)
        # expected result:
        # ZF = 1 as the result is zero
        # NF = 0 as the value is <= 0x4F
        self.checkRegisters(CPUCopy, 1, 0, 0, 0)

        # Test 3
        test_value_mem = 0x40
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.INC_Absolute(3)
        # expected result:
        # ZF = 0 as the result is not zero
        # NF = 0 as the value is <= 0x4F
        self.checkRegisters(CPUCopy, 0, 0, 0, 0)

        print("Complete: test_INCAbsolute =======")
        del CPUCopy

    def test_INCAbsoluteWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        test_value_mem = 0xAA
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.INC_AbsoluteWithX(3)
        # Mem + addr(reg) = mem + 1
        # expected result:
        # ZF = 0 as the result is not zero
        # NF = 1 as the value is >= 0x4F
        self.checkRegisters(CPUCopy, 0, 1, 0, 0)

        # Test 2
        test_value_mem = 0xFF
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.INC_AbsoluteWithX(3)
        # expected result:
        # ZF = 1 as the result is zero
        # NF = 0 as the value is <= 0x4F
        self.checkRegisters(CPUCopy, 1, 0, 0, 0)

        # Test 3
        test_value_mem = 0x40
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.INC_AbsoluteWithX(3)
        # expected result:
        # ZF = 0 as the result is not zero
        # NF = 0 as the value is <= 0x4F
        self.checkRegisters(CPUCopy, 0, 0, 0, 0)

        print("Complete: test_INCAbsoluteWithX =======")
        del CPUCopy


"""
 INX - Increment X Register			
			
X,Z,N = X+1			
			
Adds one to the X register setting the zero and negative flags as appropriate.			
			
Processor Status after use:			
			
C	Carry Flag	Not affected	
Z	Zero Flag	Set if X is zero	
I	Interrupt Disable	Not affected
D	Decimal Mode Flag	Not affected	
B	Break Command	Not affected	
V	Overflow Flag	Not affected	
N	Negative Flag	Set if bit 7 of X is set	
			
Addressing Mode	Opcode	Bytes	Cycles
Implied	$E8	1	2
"""


def test_INCXImplied(self):
    # For comparison at the end to ensure not inadvertent register flags changed
    CPUCopy = copy.deepcopy(self.processor)

    test_value_mem = 0xAA
    instructions = (
        [0xFFFC, 0x2D],
        [0xFFFD, 0x20],
        [0xFFFE, 0x00],
        [0x0030, test_value_mem],
    )
    self.programSetup(instructions)
    self.processor.X = 0x10
    self.processor.INC_Implied(3)
    # Mem + addr(reg) = mem + 1
    # expected result:
    # ZF = 0 as the result is not zero
    # NF = 1 as the value is >= 0x4F
    self.checkRegisters(CPUCopy, 0, 1, 0, 0)

    # Test 2
    test_value_mem = 0xFF
    instructions = (
        [0xFFFC, 0x2D],
        [0xFFFD, 0x20],
        [0xFFFE, 0x00],
        [0x0030, test_value_mem],
    )
    self.programSetup(instructions)
    self.processor.X = 0x10
    self.processor.INC_AbsoluteWithX(3)
    # expected result:
    # ZF = 1 as the result is zero
    # NF = 0 as the value is <= 0x4F
    self.checkRegisters(CPUCopy, 1, 0, 0, 0)

    # Test 3
    test_value_mem = 0x40
    instructions = (
        [0xFFFC, 0x2D],
        [0xFFFD, 0x20],
        [0xFFFE, 0x00],
        [0x0030, test_value_mem],
    )
    self.programSetup(instructions)
    self.processor.X = 0x10
    self.processor.INC_AbsoluteWithX(3)
    # expected result:
    # ZF = 0 as the result is not zero
    # NF = 0 as the value is <= 0x4F
    self.checkRegisters(CPUCopy, 0, 0, 0, 0)

    print("Complete: test_INCAbsoluteWithX =======")
    del CPUCopy
