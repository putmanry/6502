"""  ========= STy Functions ========= """
from instructions.instruction_base import Instruction
import logging


class STY(Instruction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("STY Init")
        pass

    def register_opcodes(self):
        self.log.debug("STY Register opcodes")
        return {
            0x84: self.MemAccess_ZeroPage,
            0x94: self.MemAccess_ZeroPageWithX,
            0x8C: self.MemAccess_Absolute,
        }

    def base_operation(value: int) -> int:
        return super().base_operation()

    def MemAccess_AbsoluteWithX(value: int) -> int:
        return super().MemAccess_AbsoluteWithX()

    def MemAccess_AbsoluteWithY(value: int) -> int:
        return super().MemAccess_AbsoluteWithY()

    def MemAccess_Immediate(value: int) -> int:
        return super().MemAccess_Immediate()

    def MemAccess_IndirectWithX(value: int) -> int:
        return super().MemAccess_IndirectWithX()

    def MemAccess_IndirectWithY(value: int) -> int:
        return super().MemAccess_IndirectWithY()

    def MemAccess_ZeroPage(self, cycles):
        self.PC += 1
        self.WriteZeroPage(cycles, self.Y)

    def MemAccess_ZeroPageWithX(self, cycles):
        self.PC += 1
        self.WriteZeroPageWithX(cycles, self.Y)

    def MemAccess_Absolute(self, cycles):
        self.PC += 1
        self.WriteAbsolute(cycles, self.Y)
