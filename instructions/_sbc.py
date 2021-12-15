"""  ========= SBC Functions ========= """
from instructions.instruction_base import Instruction
import logging


class SBC(Instruction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("SBC Init")
        pass

    def register_opcodes(self):
        self.log.debug("SBC Register opcodes")
        return {
            0xE9: self.MemAccess_Immediate,
            0xE5: self.MemAccess_ZeroPage,
            0xF5: self.MemAccess_ZeroPageWithX,
            0xED: self.MemAccess_Absolute,
            0xFD: self.MemAccess_AbsoluteWithX,
            0xF9: self.MemAccess_AbsoluteWithY,
            0xE1: self.MemAccess_IndirectWithX,
            0xF1: self.MemAccess_IndirectWithY,
        }

    # Do the basic function of SBC
    #  A-M-(1-C)
    def base_operation(self, cycles, value):
        result = self.A - value - (1 - self.CF)
        # ZF set if A = 0
        self.ZF = int(result == 0)
        # NF set if bit 7 is set
        # but since this is python, check if just negative instead
        self.NF = int(result < 0)

        # CF clear if overflow in bit 7
        # OF set if the sign bit is incorrect
        if (result > 0xFF) | (result < 0x00):
            self.CF = 0
            self.OF = 1
        self.A = result & 0x00FF

    def MemAccess_Immediate(self, cycles):
        self.PC += 1
        value, cycles = self.ReadImmediate(self.PC)
        self.base_operation(cycles, value)
        return cycles

    def MemAccess_ZeroPage(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPage(self.PC)
        self.base_operation(cycles, value)
        return cycles

    def MemAccess_ZeroPageWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPageWithX(cycles)
        self.base_operation(cycles, value)
        return cycles

    def MemAccess_Absolute(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsolute(cycles)
        self.base_operation(cycles, value)
        return cycles

    def MemAccess_AbsoluteWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithX(cycles)
        self.base_operation(cycles, value)
        return cycles

    def MemAccess_AbsoluteWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithY(cycles)
        self.base_operation(cycles, value)
        return cycles

    def MemAccess_IndirectWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadIndirectWithX(cycles)
        self.base_operation(cycles, value)
        return cycles

    def MemAccess_IndirectWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadIndirectWithY(cycles)
        self.base_operation(cycles, value)
        return cycles
