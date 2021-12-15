"""  ========= ADC Functions ========= """
from instructions.instruction_base import Instruction
import logging


class ADC(Instruction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("ADC Init")
        pass

    def register_opcodes(self):
        self.log.debug("ADC Register opcodes")
        return {
            0x69: self.MemAccess_Immediate,
            0x65: self.MemAccess_ZeroPage,
            0x75: self.MemAccess_ZeroPageWithX,
            0x6D: self.MemAccess_Absolute,
            0x7D: self.MemAccess_AbsoluteWithX,
            0x79: self.MemAccess_AbsoluteWithY,
            0x61: self.MemAccess_IndirectWithX,
            0x71: self.MemAccess_IndirectWithY,
        }

    # Do the basic function of ADC
    # http://www.righto.com/2012/12/the-6502-overflow-flag-explained.html
    # http://www.righto.com/2013/01/a-small-part-of-6502-chip-explained.html
    # http://www.6502.org/tutorials/vflag.html
    # From the MCS6500 microcomputer family programming manual:
    # Set the carry flag when the sum of a binary add exceeds 255 or when the sum of a
    # a decimal add exceeds 99, otherwise the carry is reset. The overflow flag is set
    # when the sign or bit 7 is changed due to the result exceeding +127 or -128, otherwise
    # overflow is reset. The negative flag is set if the accumulatory result contains bit 7
    # on, otherwise the negative flag is reset. The zero flag is set if the acumulator
    # result is 0, otherwise the zero flag is reset.

    def base_operation(self, cycles, value):
        result = self.A + value + self.CF
        self.CF = int(result > 0xFF)
        self.OF = int((result > 127) | (result < -128))
        # mask off any bits above an 8 bit value since
        # self.A is only 8 bits.
        self.A = result & 0x00FF
        self.ZF = int(self.A == 0)
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
