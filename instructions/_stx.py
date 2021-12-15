"""  ========= STX Functions ========= """
from instructions.instruction_base import Instruction
import logging


class STX(Instruction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("STX Init")
        pass

    def register_opcodes(self):
        self.log.debug("STX Register opcodes")
        return {
            0x86: self.MemAccess_ZeroPage,
            0x96: self.MemAccess_ZeroPageWithY,
            0x8E: self.MemAccess_Absolute,
        }

    def base_operation(value: int) -> int:
        return super().base_operation()

    def MemAccess_AbsoluteWithX(value: int) -> int:
        return super().MemAccess_AbsoluteWithX()

    def MemAccess_Immediate(value: int) -> int:
        return super().MemAccess_Immediate()

    def MemAccess_AbsoluteWithY(value: int) -> int:
        return super().MemAccess_AbsoluteWithY()

    def MemAccess_IndirectWithX(value: int) -> int:
        return super().MemAccess_IndirectWithX()

    def MemAccess_IndirectWithY(value: int) -> int:
        return super().MemAccess_IndirectWithY()

    def MemAccess_ZeroPageWithX(value: int) -> int:
        return super().MemAccess_ZeroPageWithX()

    def MemAccess_ZeroPage(self, cycles):
        self.PC += 1
        self.WriteZeroPage(cycles, self.X)

    def MemAccess_ZeroPageWithY(self, cycles):
        self.PC += 1
        self.WriteZeroPageWithY(cycles, self.X)

    def MemAccess_Absolute(self, cycles):
        self.PC += 1
        self.WriteAbsolute(cycles, self.X)
