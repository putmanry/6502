from architecture.processor import CPU_6502
import copy
import _BaseTest


class Test_CMPXInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """
    CPX - Compare X Register			
			
    Z,C,N = X-M			
                
    This instruction compares the contents of the X register with another memory held value and sets the zero and carry flags as appropriate.			
                
    Processor Status after use:			
                
    C	Carry Flag	Set if X >= M	
    Z	Zero Flag	Set if X = M	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break Command	Not affected	
    V	Overflow Flag	Not affected	
    N	Negative Flag	Set if bit 7 of the result is set	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Immediate	$E0	2	2
    Zero Page	$E4	2	3
    Absolute	$EC	3	4
                
    See also: CMP, CPY			
			
    """

    def test_CMPXImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x69], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = test_value_reg
        self.processor.CMPX_Immediate(3)

        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is >= 0
        # NF = 0 as the value is not negative
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x69], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = test_value_reg
        self.processor.CMPX_Immediate(3)

        # 0x00 - 0xAA = 0xAA
        # expected result:
        # ZF = 0 as A != M
        # CF = 0 as A <= M
        # NF = 1 as the result is neg
        self.checkRegisters(CPUCopy, 0, 1, 0, 0)

        # Test 3
        test_value_mem = 0x40
        test_value_reg = 0x4A
        instructions = ([0xFFFC, 0x69], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = test_value_reg
        self.processor.CMPX_Immediate(3)

        # 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMPImmediate=======")
        del CPUCopy

    def test_CMPXZeroPage(self):
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = test_value_reg
        self.processor.CMPX_ZeroPage(3)

        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is >= 0
        # NF = 0 as the value is not negative
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = test_value_reg
        self.processor.CMPX_ZeroPage(3)

        # 0x00 - 0xAA = 0xAA
        # expected result:
        # ZF = 0 as A != M
        # CF = 0 as A <= M
        # NF = 1 as the result is neg
        self.checkRegisters(CPUCopy, 0, 1, 0, 0)

        # Test 3
        test_value_mem = 0x40
        test_value_reg = 0x4A
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = test_value_reg
        self.processor.CMPX_ZeroPage(3)

        # 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMPZeroPage=======")
        del CPUCopy

    def test_CMPXAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.X = test_value_reg
        self.processor.CMPX_Absolute(3)

        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is >= 0
        # NF = 0 as the value is not negative
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.X = test_value_reg
        self.processor.CMPX_Absolute(3)
        # 0x00 - 0xAA = 0xAA
        # expected result:
        # ZF = 0 as A != M
        # CF = 0 as A <= M
        # NF = 1 as the result is neg
        self.checkRegisters(CPUCopy, 0, 1, 0, 0)

        # Test 3
        test_value_mem = 0x40
        test_value_reg = 0x4A
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0020, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.X = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.CMPX_Absolute(3)
        # 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMPAbsolute =======")
        del CPUCopy
