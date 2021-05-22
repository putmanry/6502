"""
6502 CPU Emulator
Using data here: http://www.obelisk.me.uk/index.html
and here: https://www.cpu-world.com/Arch/650x.html
"""
from ._memory import _MemoryMixin
from ._addressing_modes import _AddressingModesMixin
from ._commands import _CommandsMixin


class CPU_6502(_MemoryMixin, _AddressingModesMixin, _CommandsMixin):
    PC = 0  # Program counter
    SP = 0  # Stack pointer
    A = 0  # Accumulator
    x = 0  # X register
    y = 0  # Y register
    Status = 0  # Processor Status


'''
TODO: Create get/set/clear/etc functions for the registers
'''

"""
    flags = 0
    CF = 1 << 0
    ZF = 1 << 1
    ID = 1 << 2
    DM = 1 << 3
    BC = 1 << 4
    Unused = 1 << 5
    OV = 1 << 6
    NF = 1 << 7
"""

'''
TODO: move registers to a class on it's own
do set/clr/test members for it
'''


    CF = 0  # Carry Flag Bit
    ZF = 0  # Zero Flag Bit
    ID = 0  # Interrupt Disable
    DM = 0  # Decimal mode
    BC = 0  # Break Command
    OF = 0  # Overflow Command
    NF = 0  # Negative Flag

    def reset(self):
        self.PC = 0xFFFC
        self.SP = 0x0100
        self.A = 0
        self.x = 0
        self.y = 0
        self.Status = 0
        self.flags = 0

        self.mem_intialize()

    def execute(self, cycles):
        self.PC = 0
        while cycles > 0:
            cmd = self.read_mem(self.PC)
            self.instructions[cmd](self)
            self.instructions[0xA9](self)
            cycles = cycles - 1
            self.PC = self.PC + 1
            print("PC %s cycles %s" % (self.PC, cycles))
        return True
