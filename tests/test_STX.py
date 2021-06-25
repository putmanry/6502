from architecture.processor import CPU_6502
import copy
import _BaseTest

"""
STX - Store X Register			
			
M = X			
			
Stores the contents of the X register into memory.			
			
Processor Status after use:	Carry Flag	Not affected	
	Zero Flag	Not affected	
C	Carry Flag	Not affected	
Z	Zero Flag	Not affected	
I	Interrupt Disable	Not affected	
D	Decimal Mode Flag	Not affected	
B	Break Command	Not affected	
V	Overflow Flag	Not affected	
N	Negative Flag	Not affected	

Addressing Mode	Opcode	Bytes	Cycles
Zero Page	$86	2	3
Zero Page,Y	$96	2	4
Absolute	$8E	3	4
"""


class Test_STXInstructions(_BaseTest._BaseTestMixin):

    __test__ = True

    def test_STXwithZeroPage(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        instructions = ([0xFFFC, 0x85], [0xFFFD, 0x10])
        self.programSetup(instructions)
        self.processor.X = 0xAA  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.STX_ZeroPage(3)
        self.assertEqual(
            self.processor.read_mem(instructions[1][1]),
            0xAA,
            "1 - STXwithZeroPage failed to store X correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_STXwithZeroPage =======")
        del CPUCopy

    def test_STXwithAbsolute(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        # Instruction contains the full 16 bit address to the identify the target location
        instructions = ([0xFFFC, 0x8D], [0xFFFD, 0x80], [0xFFFE, 0x44])
        self.programSetup(instructions)
        self.processor.X = 0xAA
        self.processor.STX_Absolute(3)
        lo_byte = instructions[1][1]
        hi_byte = instructions[2][1]
        location = hi_byte << 8 | lo_byte
        self.assertEqual(
            self.processor.read_word_address(location),
            0xAA,
            "1 - STXwithAbsolute failed to store A correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_STXwithAbsolute =======")
        del CPUCopy

    def test_STXwithZeroPageWithY(self):
        # For comparison at the end to ensure not inadvertent register flags changed
        CPUCopy = copy.deepcopy(self.processor)

        # Test 1 -
        instructions = ([0xFFFC, 0x85], [0xFFFD, 0x10])
        self.programSetup(instructions)
        self.processor.Y = 0x10
        self.processor.X = 0xAA  # Has to come after programSetup due to reset processor clearing registers.
        self.processor.STX_ZeroPageWithY(3)
        self.assertEqual(
            self.processor.read_mem(instructions[1][1] + self.processor.Y),
            0xAA,
            "1 - STXwithZeroPageWithY failed to store X correctly",
        )
        self.checkRegisters(CPUCopy, CPUCopy.ZF, CPUCopy.NF)

        print("Complete: test_STXwithZeroPagewithY =======")
        del CPUCopy
