from architecture.processor import CPU_6502
import copy
import _BaseTest


class Test_CMPInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    """
    CMP - Compare
			
    Z,C,N = A-M			
                
    This instruction compares the contents of the accumulator with another memory held value and sets the zero and carry flags as appropriate.			
                
    Processor Status after use:			
                
    C	Carry Flag	Set if A >= M	
    Z	Zero Flag	Set if A = M	
    I	Interrupt Disable	Not affected	
    D	Decimal Mode Flag	Not affected	
    B	Break Command	Not affected	
    V	Overflow Flag	Not affected	
    N	Negative Flag	Set if bit 7 of the result is set	
                
    Addressing Mode	Opcode	Bytes	Cycles
    Immediate	$C9	2	2
    Zero Page	$C5	2	3
    Zero Page,X	$D5	2	4
    Absolute	$CD	3	4
    Absolute,X	$DD	3	4 (+1 if page crossed)
    Absolute,Y	$D9	3	4 (+1 if page crossed)
    (Indirect,X)	$C1	2	6
    (Indirect),Y	$D1	2	5 (+1 if page crossed)
			
    """

    def test_CMPImmediate(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x69], [0xFFFD, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CMP_Immediate(3)

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
        self.processor.A = test_value_reg
        self.processor.CMP_Immediate(3)

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
        self.processor.A = test_value_reg
        self.processor.CMP_Immediate(3)

        # 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMPImmediate=======")
        del CPUCopy

    def test_CMPZeroPage(self):
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1
        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x25], [0xFFFD, 0x10], [0x0010, test_value_mem])
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.CMP_ZeroPage(3)

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
        self.processor.A = test_value_reg
        self.processor.CMP_ZeroPage(3)

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
        self.processor.A = test_value_reg
        self.processor.CMP_ZeroPage(3)

        # 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMPZeroPage=======")
        del CPUCopy

    def test_CMPZeroPageWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = ([0xFFFC, 0x75], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg
        self.processor.CMP_ZeroPageWithX(3)

        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is >= 0
        # NF = 0 as the value is not negative
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

        # Test 2
        test_value_mem = 0xAA
        test_value_reg = 0x00
        instructions = ([0xFFFC, 0x75], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg
        self.processor.CMP_ZeroPageWithX(3)
        # 0x00 - 0xAA = 0xAA
        # expected result:
        # ZF = 0 as A != M
        # CF = 0 as A <= M
        # NF = 1 as the result is neg
        self.checkRegisters(CPUCopy, 0, 1, 0, 0)

        # Test 3
        test_value_mem = 0x40
        test_value_reg = 0x4A
        instructions = ([0xFFFC, 0x75], [0xFFFD, 0x10], [0x0020, test_value_mem])
        self.programSetup(instructions)
        self.processor.X = 0x10
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.CMP_ZeroPageWithX(3)
        # 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMPZeroPageWithX =======")
        del CPUCopy

    def test_CMPAbsolute(self):
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
        self.processor.A = test_value_reg
        self.processor.CMP_Absolute(3)

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
        self.processor.A = test_value_reg
        self.processor.CMP_Absolute(3)
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
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.CMP_Absolute(3)
        # 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMPAbsolute =======")
        del CPUCopy

    def test_CMPAbsoluteWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        test_value_mem = 0xAA
        test_value_reg = 0xAA
        instructions = (
            [0xFFFC, 0x2D],
            [0xFFFD, 0x20],
            [0xFFFE, 0x00],
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x10
        self.processor.CMP_AbsoluteWithX(3)

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
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x10
        self.processor.CMP_AbsoluteWithX(3)
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
            [0x0030, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.X = 0x10
        self.processor.CMP_AbsoluteWithX(3)
        # 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMPAbsoluteWithX =======")
        del CPUCopy

    def test_CMPAbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

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
        self.processor.CMP_IndirectWithY(3)

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
            [0xFFFC, 0x31],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.CMP_IndirectWithY(3)
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
            [0xFFFC, 0x31],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.CMP_IndirectWithY(3)
        # 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMPAbsoluteWithY =======")
        del CPUCopy

    def test_CMPIndirectWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

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
        self.processor.CMP_IndirectWithX(3)

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
            [0xFFFC, 0x21],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x04
        self.processor.CMP_IndirectWithX(3)
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
            [0xFFFC, 0x21],
            [0xFFFD, 0x02],
            [0x0006, 0x00],
            [0x0007, 0x80],
            [0x8000, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.A = test_value_reg
        self.processor.X = 0x04
        self.processor.CMP_IndirectWithX(3)
        # 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMPIndirectWithX =======")
        del CPUCopy

    def test_CMPIndirectWithY(self):
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
        self.processor.CMP_IndirectWithY(3)

        # 0xAA - 0xAA = 0x00
        # expected result:
        # ZF = 1 as the result is zero
        # CF = 1 as the result is >= 0
        # NF = 0 as the value is not negative
        self.checkRegisters(CPUCopy, 1, 0, 1, 0)

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
        self.processor.CMP_IndirectWithY(3)

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
            [0xFFFC, 0x31],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
            [0x403A, test_value_mem],
        )
        self.programSetup(instructions)
        self.processor.Y = 0xE9
        self.processor.A = test_value_reg
        self.processor.CMP_IndirectWithY(3)

        ## 0x4A - 0x40 = 0x0A
        # expected result:
        # ZF = 0 as A != M
        # CF = 1 as A >= M
        # NF = 0 as result is positive
        self.checkRegisters(CPUCopy, 0, 0, 1, 0)

        print("Complete: test_CMP_IndirectWithY =======")
        del CPUCopy
