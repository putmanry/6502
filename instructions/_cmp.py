"""  ========= CMP Functions ========= """
from instructions.instruction_base import Instruction
import logging


class CMP(Instruction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("CMP Init")
        pass

    def register_opcodes(self):
        self.log.debug("CMP Register opcodes")
        return {
            0xC9: self.MemAccess_Immediate,
            0xC5: self.MemAccess_ZeroPage,
            0xD5: self.MemAccess_ZeroPageWithX,
            0xCD: self.MemAccess_Absolute,
            0xDD: self.MemAccess_AbsoluteWithX,
            0xD9: self.MemAccess_AbsoluteWithY,
            0xC1: self.MemAccess_IndirectWithX,
            0xD1: self.MemAccess_IndirectWithY,
        }

    # Do the basic function of CMP
    def base_operation(self, cycles, value):
        if self.A >= value:
            self.CF = 1
        if self.A == value:
            self.ZF = 1
        if (self.A - value) < 0:
            self.NF = 1

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
