'''
6502 CPU Emulator
Using data here: http://www.obelisk.me.uk/index.html
and here: https://www.cpu-world.com/Arch/650x.html
'''
from ._memory import _MemoryMixin
from ._addressing_modes import _AddressingModesMixin


class CPU_6502 (_MemoryMixin, _AddressingModesMixin):
    PC = 0      # Program counter
    SP = 0      # Stack pointer
    Acc = 0     # Accumulator
    x = 0      # X register
    y = 0       # Y register
    Status = 0  # Processor Status

    CF = 0      # Carry Flag Bit
    ZF = 0      # Zero Flag Bit
    ID = 0      # Interrupt Disable
    DM = 0      # Decimal mode
    BC = 0      # Break Command
    OF = 0      # Overflow Command
    NF = 0      # Negative Flag


    def execute(cycles, command):
        return True
    
    