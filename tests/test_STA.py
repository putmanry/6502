from architecture.processor import CPU_6502
import copy
import _BaseTest

"""
STA - Store Accumulator			
			
M = A			
			
Stores the contents of the accumulator into memory.			
			
Processor Status after use:			
			
C	Carry Flag	Not affected	
Z	Zero Flag	Not affected	
I	Interrupt Disable	Not affected	
D	Decimal Mode Flag	Not affected	
B	Break Command	Not affected	
V	Overflow Flag	Not affected	
N	Negative Flag	Not affected	
			
Addressing Mode	Opcode	Bytes	Cycles
Zero Page	$85	2	3
Zero Page,X	$95	2	4
Absolute	$8D	3	4
Absolute,X	$9D	3	5
Absolute,Y	$99	3	5
(Indirect,X)	$81	2	6
(Indirect),Y	$91	2	6
"""


class Test_STAInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    def test_STAwithZeroPage(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        instructions = ([0xFFFC, 0x85], [0xFFFD, 0x10])
        self.programSetup(instructions)
        self.processor.A = 0xAA  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.STA_ZeroPage(3)
        self.assertEqual(
            self.processor.read_mem(instructions[1][1]),
            0xAA,
            "1 - STAwithZeroPage failed to store A correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_STAwithZeroPage =======")
        del CPUCopy

    def test_STAwithZeroPageX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        instructions = ([0xFFFC, 0x95], [0xFFFD, 0x10])
        self.programSetup(instructions)
        self.processor.A = 0xAA
        self.processor.X = 0x0F
        self.processor.STA_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.read_mem(instructions[1][1] + self.processor.X),
            0xAA,
            "1 - STAwithZeroPageWithX failed to store A correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_STAwithZeroPageWithX =======")
        del CPUCopy

    def test_STAwithAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Instruction contains the full 16 bit address to the identify the target location
        instructions = ([0xFFFC, 0x8D], [0xFFFD, 0x80], [0xFFFE, 0x44])
        self.programSetup(instructions)
        self.processor.A = 0xAA
        self.processor.STA_Absolute(3)
        loc_lo = instructions[1][1]
        loc_hi = instructions[2][1]
        value = loc_hi << 8 | loc_lo
        self.assertEqual(
            self.processor.read_word_address(value),
            0xAA,
            "1 - STAwithAbsolute failed to store A correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_STAwithAbsolute =======")
        del CPUCopy

    def test_STAAbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        instructions = ([0xFFFC, 0x8D], [0xFFFD, 0x80], [0xFFFE, 0x44])
        self.programSetup(instructions)
        self.processor.A = 0xAA
        self.processor.Y = 0x0F
        self.processor.STA_AbsoluteWithY(3)
        loc_lo = instructions[1][1]
        loc_hi = instructions[2][1]
        value = loc_hi << 8 | loc_lo + self.processor.Y
        self.assertEqual(
            self.processor.read_word_address(value),
            0xAA,
            "1 - STAAbsoluteWithY failed to save A",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: STAAbsoluteWithY=======")
        del CPUCopy

    def test_STAAbsoluteWithX(self):
        CPUCopy = copy.deepcopy(self.processor)

        instructions = ([0xFFFC, 0x8D], [0xFFFD, 0x80], [0xFFFE, 0x44])
        self.programSetup(instructions)
        self.processor.A = 0xAA
        self.processor.X = 0x0F
        self.processor.STA_AbsoluteWithX(3)
        loc_lo = instructions[1][1]
        loc_hi = instructions[2][1]
        value = loc_hi << 8 | loc_lo + self.processor.X
        self.assertEqual(
            self.processor.read_word_address(value),
            0xAA,
            "1 - STAAbsoluteWithX failed to save A",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: STAAbsoluteWithX=======")
        del CPUCopy

    def test_STAIndirectWithX(self):
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        instructions = ([0xFFFC, 0x81], [0xFFFD, 0x10])
        self.programSetup(instructions)
        self.processor.A = 0xAA
        self.processor.X = 0x04
        self.processor.STA_IndirectWithX(3)
        self.assertEqual(
            self.processor.read_mem(instructions[1][1] + self.processor.X),
            0xAA,
            "1 - STAIndirectWithX failed to load A",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)
        print("Complete: STAIndirectWithX=======")
        del CPUCopy

    def test_STAIndirectWithY(self):
        CPUCopy = copy.deepcopy(self.processor)

        # TODO: This needs lots of work.
        # Test 1 -
        instructions = (
            [0xFFFC, 0x81],
            [0xFFFD, 0xA4],
            [0x00A4, 0x51],
            [0x00A5, 0x3F],
        )
        self.programSetup(instructions)
        self.processor.A = 0xAA
        self.processor.Y = 0x04
        self.processor.STA_IndirectWithY(3)
        loc_lo = instructions[2][1]
        loc_hi = instructions[3][1]
        value = loc_hi << 8 | loc_lo + self.processor.Y
        self.assertEqual(
            self.processor.read_mem(value),
            0xAA,
            "1 - STAIndirectWithY failed to load A",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)
        print("Complete: STAIndirectWithY=======")
        del CPUCopy
