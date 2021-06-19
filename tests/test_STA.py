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

    def test_AbsoluteWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # If X containes 0x92 and we have an STA 0x2000, X the instruction will load from
        # 0x2092.
        instructions = ([0xFFFC, 0xBE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x82])
        self.processor.Y = 0x0F
        self.programSetup(instructions)
        self.processor.STA_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.X, 0x82, "1 - STAAbsoluteWithY failed to load X"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, 1)

        # Test 2 -
        # For 0x32 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xBE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x32])
        self.processor.Y = 0x0F
        self.programSetup(instructions)
        self.processor.STA_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.X, 0x32, "2 - STAAbsoluteWithY failed to load X"
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        # Test 3 -
        # For 0x00 - ZF shoudl not change and NF should not change
        instructions = ([0xFFFC, 0xBE], [0xFFFD, 0x80], [0xFFFE, 0x44], [0x448F, 0x00])
        self.processor.Y = 0x0F
        self.programSetup(instructions)
        self.processor.STA_AbsoluteWithY(3)
        self.assertEqual(
            self.processor.X, 0x00, "2 - STAAbsoluteWithY failed to load X"
        )
        self.checkRegisters(CPUCopy, 1, CPUCopy.NF)

        # TODO: need to deal with wrapping at top end.

        print("Complete: STAAbsoluteWithY=======")
        del CPUCopy
