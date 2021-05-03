'''
6502 CPU Emulator
Using data here: http://www.obelisk.me.uk/index.html
and here: https://www.cpu-world.com/Arch/650x.html
'''
from architecture._addressing_modes import _addressing_modes
from architecture._memory import _memory

'_addressing_modes.Mixin, _memory.Mixin'

class CPU_6502 ():
    PC      # Program counter
    SP      # Stack pointer
    Acc     # Accumulator
    x       # X register
    y       # Y register
    Status  # Processor Status

    CF      # Carry Flag Bit
    ZF      # Zero Flag Bit
    ID      # Interrupt Disable
    DM      # Decimal mode
    BC      # Break Command
    OF      # Overflow Command
    NF      # Negative Flag

    def __init__(self):
        return True
    
    def execute(cycles, command):
        return True

    
