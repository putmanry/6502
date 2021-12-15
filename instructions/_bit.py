"""  ========= BIT Functions ========= """
from instructions.instruction_base import Instruction
import logging


class BIT(Instruction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("BIT Init")
        pass

    def register_opcodes(self):
        self.log.debug("BIT Register opcodes")
        return {
            0x24: self.MemAccess_ZeroPage,
            0x2C: self.MemAccess_Absolute,
        }

    def base_operation(self, cycles, value):
        result = self.A & value
        if result == 0:
            self.ZF = 0
        bit_7 = (value & 0b10000000) >> 7
        self.NF = bit_7
        bit_6 = (value & 0b01000000) >> 6
        self.OF = bit_6

    def MemAccess_ZeroPage(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPage(self.PC)
        self.base_operation(cycles, value)
        return cycles

    def MemAccess_Absolute(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsolute(cycles)
        self.base_operation(cycles, value)
        return cycles

    def MemAccess_AbsoluteWithX(self, cycles):
        return cycles

    def MemAccess_AbsoluteWithY(self, cycles):
        return cycles

    def MemAccess_Immediate(self, cycles):
        return cycles

    def MemAccess_IndirectWithX(self, cycles):
        return cycles

    def MemAccess_IndirectWithY(self, cycles):
        return cycles

    def MemAccess_ZeroPageWithX(self, cycles):
        return cycles
