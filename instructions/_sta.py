"""  ========= STA Functions ========= """
from instructions.instruction_base import Instruction
import logging


class STA(Instruction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("STA Init")
        pass

    def register_opcodes(self):
        self.log.debug("STA Register opcodes")
        return {
            0x85: self.MemAccess_ZeroPage,
            0x95: self.MemAccess_ZeroPageWithX,
            0x8D: self.MemAccess_Absolute,
            0x9D: self.MemAccess_AbsoluteWithX,
            0x99: self.MemAccess_AbsoluteWithY,
            0x81: self.MemAccess_IndirectWithX,
            0x91: self.MemAccess_IndirectWithY,
        }

    def base_operation(value: int) -> int:
        return super().base_operation()

    def MemAccess_Immediate(value: int) -> int:
        return super().MemAccess_Immediate()

    def MemAccess_ZeroPage(self, cycles):
        self.PC += 1
        self.WriteZeroPage(cycles, self.A)

    def MemAccess_ZeroPageWithX(self, cycles):
        self.PC += 1
        self.WriteZeroPageWithX(cycles, self.A)

    def MemAccess_Absolute(self, cycles):
        self.PC += 1
        self.WriteAbsolute(cycles, self.A)

    def MemAccess_AbsoluteWithX(self, cycles):
        self.PC += 1
        self.WriteAbsoluteWithX(cycles, self.A)

    def MemAccess_AbsoluteWithY(self, cycles):
        self.PC += 1
        self.WriteAbsoluteWithY(cycles, self.A)

    def MemAccess_IndirectWithX(self, cycles):
        self.PC += 1
        self.WriteIndirectWithX(cycles, self.A)

    def MemAccess_IndirectWithY(self, cycles):
        self.PC += 1
        self.WriteIndirectWithY(cycles, self.A)
