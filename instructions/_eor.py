"""  ========= EOR Functions ========= """
from instructions.instruction_base import Instruction
import logging


class EOR(Instruction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("EOR Init")
        pass

    def register_opcodes(self):
        self.log.debug("EOR Register opcodes")
        return {
            0x49: self.MemAccess_Immediate,
            0x45: self.MemAccess_ZeroPage,
            0x55: self.MemAccess_ZeroPageWithX,
            0x4D: self.MemAccess_Absolute,
            0x5D: self.MemAccess_AbsoluteWithX,
            0x59: self.MemAccess_AbsoluteWithY,
            0x41: self.MemAccess_IndirectWithX,
            0x51: self.MemAccess_IndirectWithY,
        }

    def base_operation(self, cycles, value):
        result = self.A ^ value
        self.A = result
        if self.A == 0:
            self.ZF = 1
        self.NF = int(self.A >= 0x40)

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
