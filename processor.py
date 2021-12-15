"""
6502 CPU Emulator
Using data here: http://www.obelisk.me.uk/index.html
and here: https://www.cpu-world.com/Arch/650x.html
and here: https://www.c64-wiki.com/
"""
from memory._memory import Memory
from instructions._commands import Commands
from _flags import Flags
import logging


class CPU_6502:
    def __init__(self) -> None:

        self.log = logging.getLogger(__name__)

        self.PC = 0  # Program counter
        self.SP = 0  # Stack pointer
        self.A = 0  # Accumulator
        self.X = 0  # X register
        self.Y = 0  # Y register
        self.Status = 0  # Processor Status
        self.flags = Flags()
        self.memory = Memory()
        self.opcodes = Commands()

    def __str__(self):
        self.log.info("__str__ repr CPU_6502")
        self.log.info("PC: 0x{:04x}      SP: 0x{:04x}".format(self.PC, self.SP))
        self.log.info(" X: 0x{:04x}       Y: 0x{:04x}".format(self.X, self.Y))
        self.log.info(" A: 0x{:04x}  Status: 0x{:04x}".format(self.A, self.Status))

    """ CPU Reset - initializes the state of the CPU """

    def reset(self):
        self.log.debug("CPU_6502: Reset")
        self.PC = 0xFFFC
        self.SP = 0x0100
        self.A = 0
        self.X = 0
        self.Y = 0
        self.Status = 0
        self.flags.flags_reset()
        self.memory.mem_intialize()
        self.opcodes.commands_initialize()

    """ CPU executes number of cycles """

    def run(self, cycles=1):

        while cycles > 0:
            cmd = self.read_mem(self.PC)
            cycles = self.instructions[cmd](self, cycles)
            cycles = cycles - 1
            self.PC = self.PC + 1
            self.log.info("PC 0x{:04x} cycles {}".format(self.PC, cycles))
        return True

    def execute_command(self, command: int) -> None:
        pass
