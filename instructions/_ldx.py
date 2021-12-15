from instructions.instruction_base import Instruction
import logging


class LDX(Instruction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("LDX Init")
        pass

    def register_opcodes(self):
        self.log.debug("LDX Register opcodes")
        return {
            0xA2: self.MemAccess_Immediate,
            0xA6: self.MemAccess_ZeroPage,
            0xB6: self.MemAccess_ZeroPageWithY,
            0xAE: self.MemAccess_Absolute,
            0xBE: self.MemAccess_AbsoluteWithY,
        }

    def base_operation(self, value):
        self.X = value
        if self.X == 0:
            self.ZF = 1
        self.NF = int(self.X >= 0x40)

    def MemAccess_ZeroPageWithX(value: int) -> int:
        return super().MemAccess_ZeroPageWithX()

    def MemAccess_AbsoluteWithX(value: int) -> int:
        return super().MemAccess_AbsoluteWithX()

    def MemAccess_AbsoluteWithY(value: int) -> int:
        return super().MemAccess_AbsoluteWithY()

    def MemAccess_IndirectWithX(value: int) -> int:
        return super().MemAccess_IndirectWithX()

    def MemAccess_IndirectWithY(value: int) -> int:
        return super().MemAccess_IndirectWithY()

    def MemAccess_Immediate(self, cycles):
        self.PC += 1
        value, cycles = self.ReadImmediate(cycles)
        self.base_operation(value)
        return cycles

    def MemAccess_Absolute(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsolute(cycles)
        self.base_operation(value)
        return cycles

    def MemAccess_ZeroPage(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPage(cycles)
        self.base_operation(value)
        return cycles

    def MemAccess_ZeroPageWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPageWithY(cycles)
        self.base_operation(value)
        return cycles

    def MemAccess_AbsoluteWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithY(cycles)
        self.base_operation(value)
        return cycles
