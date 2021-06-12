"""
6502 CPU Emulator
Using data here: http://www.obelisk.me.uk/index.html
and here: https://www.cpu-world.com/Arch/650x.html
and here: https://www.c64-wiki.com/
"""
from ._memory import _MemoryMixin
from ._addressing_modes import _AddressingModesMixin
from ._commands import _CommandsMixin
from ._flags import _FlagsMixin


class CPU_6502(_MemoryMixin, _AddressingModesMixin, _CommandsMixin, _FlagsMixin):
    def __init__(self) -> None:
        super().__init__()
        self.PC = 0  # Program counter
        self.SP = 0  # Stack pointer
        self.A = 0  # Accumulator
        self.x = 0  # X register
        self.y = 0  # Y register
        self.Status = 0  # Processor Status

    def __str__(self):
        print("PC: 0x{:04x}      SP: 0x{:04x}".format(self.PC, self.SP))
        print(" X: 0x{:04x}       Y: 0x{:04x}".format(self.x, self.y))
        print(" A: 0x{:04x}  Status: 0x{:04x}".format(self.A, self.Status))

    """ CPU Reset - initializes the state of the CPU """

    def reset(self):
        self.PC = 0xFFFC
        self.SP = 0x0100
        self.A = 0
        self.x = 0
        self.y = 0
        self.Status = 0
        self.flags = 0
        self.flags_reset()

        self.mem_intialize()

    """ CPU executes number of cycles """

    def execute(self, cycles=1):

        while cycles > 0:
            cmd = self.read_mem(self.PC)
            cycles = self.instructions[cmd](self, cycles)
            cycles = cycles - 1
            self.PC = self.PC + 1
            print("PC 0x{:04x} cycles {}".format(self.PC, cycles))
        return True

    # ======================= Getter/Setters ===================
    """ Getter/Setter for the PC Register """

    @property
    def PC(self):
        return self._PC

    @PC.setter
    def PC(self, value):
        self._PC = value

    """ Getter/Setter for the SP Register """

    @property
    def SP(self):
        return self._SP

    @SP.setter
    def SP(self, value):
        self._SP = value

    """ Getter/Setter for the A Register """

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        self._A = value

    """ Getter/Setter for the X Register """

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, value):
        self._X = value

    """ Getter/Setter for the Y Register """

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, value):
        self._Y = value

    """ Getter/Setter for the Status Register """

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, value):
        self._Status = value
