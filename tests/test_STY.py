from architecture.processor import CPU_6502
import copy
import _BaseTest

"""
STY - Store Y Register			
			
M = Y			
			
Stores the contents of the Y register into memory.			
			
Processor Status after use:			
			
C	Carry Flag	Not affected	
Z	Zero Flag	Not affected	
I	Interrupt Disable	Not affected	
D	Decimal Mode Flag	Not affected	
B	Break Command	Not affected	
V	Overflow Flag	Not affected	
N	Negative Flag	Not affected	
			
Addressing Mode	Opcode	Bytes	Cycles
Zero Page	$84	2	3
Zero Page,X	$94	2	4
Absolute	$8C	3	4
"""


class Test_STYInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    def test_STYwithZeroPage(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        instructions = ([0xFFFC, 0x85], [0xFFFD, 0x10])
        self.programSetup(instructions)
        self.processor.Y = 0xAA  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.STY_ZeroPage(3)
        self.assertEqual(
            self.processor.read_mem(instructions[1][1]),
            0xAA,
            "1 - STYwithZeroPage failed to store X correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_STYwithZeroPage =======")
        del CPUCopy

    def test_STYwithAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Instruction contains the full 16 bit address to the identify the target location
        instructions = ([0xFFFC, 0x8D], [0xFFFD, 0x80], [0xFFFE, 0x44])
        self.programSetup(instructions)
        self.processor.Y = 0xAA
        self.processor.STY_Absolute(3)
        lo_byte = instructions[1][1]
        hi_byte = instructions[2][1]
        location = hi_byte << 8 | lo_byte
        self.assertEqual(
            self.processor.read_word_address(location),
            0xAA,
            "1 - STYwithAbsolute failed to store A correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_STYwithAbsolute =======")
        del CPUCopy

    def test_STYwithZeroPageWithX(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        instructions = ([0xFFFC, 0x85], [0xFFFD, 0x10])
        self.programSetup(instructions)
        self.processor.Y = 0xAA
        self.processor.X = 0x10  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.STY_ZeroPageWithX(3)
        self.assertEqual(
            self.processor.read_mem(instructions[1][1] + self.processor.X),
            0xAA,
            "1 - STYwithZeroPageWithY failed to store X correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_STYwithZeroPagewithY =======")
        del CPUCopy
