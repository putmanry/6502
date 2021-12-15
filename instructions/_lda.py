"""  ========= LDA Functions ========= """
from instructions.instruction_base import Instruction
import logging


class LDA(Instruction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("LDA Init")
        pass

    # What LDA normally does.
    def base_operation(self, value):
        self.log.debug("LDA Base Function value={value}")
        self.A = value
        if self.A == 0:
            self.ZF = 1
        self.NF = int(self.A >= 0x40)

    # LDA with Zero page addressing.
    def MemAccess_ZeroPage(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPage(cycles)
        self.base_operation(value)
        return cycles

    # Handles LDA with Immediate load
    def MemAccess_Immediate(self, cycles):
        self.PC += 1
        value, cycles = self.ReadImmediate(cycles)
        self.base_operation(value)
        return cycles

    def MemAccess_ZeroPageWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPageWithX(cycles)
        self.base_operation(value)
        return cycles

    def MemAccess_Absolute(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsolute(cycles)
        self.base_operation(value)
        return cycles

    def MemAccess_AbsoluteWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithX(cycles)
        self.base_operation(value)
        return cycles

    def MemAccess_AbsoluteWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithY(cycles)
        self.base_operation(value)
        return cycles

    def MemAccess_IndirectWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadIndirectWithX(cycles)
        self.base_operation(value)
        return cycles

    def MemAccess_IndirectWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadIndirectWithY(cycles)
        self.base_operation(value)
        return cycles

    def register_opcodes(self):
        self.log.debug("LDA Register opcodes")
        return {
            0xA9: self.MemAccess_Immediate,
            0xA5: self.MemAccess_ZeroPage,
            0xB5: self.MemAccess_ZeroPageWithX,
            0xAD: self.MemAccess_Absolute,
            0xBD: self.MemAccess_AbsoluteWithX,
            0xB9: self.MemAccess_AbsoluteWithY,
            0xA1: self.MemAccess_IndirectWithX,
            0xB1: self.MemAccess_IndirectWithY,
        }
