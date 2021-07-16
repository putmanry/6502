"""
All the processor instructions
"""

# reread: https://stackoverflow.com/questions/47561840/python-how-can-i-separate-functions-of-class-into-multiple-files


class _CommandsMixin:

    """
    Next are all the functions that handle what each opcode does
    these funcitons have to come before the instructions dictionaty
    """

    def NOP(self, cycles):
        print("Not implemented")
        return cycles

    """  ========= LDA Functions ========= """

    # What LDA normally does.
    def LDA(self, value):
        self.A = value
        if self.A == 0:
            self.ZF = 1
        self.NF = int(self.A >= 0x40)

    # LDA with Zero page addressing.
    def LDA_ZeroPage(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPage(cycles)
        self.LDA(value)
        return cycles

    # Handles LDA with Immediate load
    def LDA_Immediate(self, cycles):
        self.PC += 1
        value, cycles = self.ReadImmediate(cycles)
        self.LDA(value)
        return cycles

    def LDA_ZeroPageWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPageWithX(cycles)
        self.LDA(value)
        return cycles

    def LDA_Absolute(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsolute(cycles)
        self.LDA(value)
        return cycles

    def LDA_AbsoluteWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithX(cycles)
        self.LDA(value)
        return cycles

    def LDA_AbsoluteWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithY(cycles)
        self.LDA(value)
        return cycles

    def LDA_IndirectWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadIndirectWithX(cycles)
        self.LDA(value)
        return cycles

    def LDA_IndirectWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadIndirectWithY(cycles)
        self.LDA(value)
        return cycles

    """  ========= LDX Functions ========= """

    def LDX(self, value):
        self.X = value
        if self.X == 0:
            self.ZF = 1
        self.NF = int(self.X >= 0x40)

    def LDX_Immediate(self, cycles):
        self.PC += 1
        value, cycles = self.ReadImmediate(cycles)
        self.LDX(value)
        return cycles

    def LDX_Absolute(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsolute(cycles)
        self.LDX(value)
        return cycles

    def LDX_ZeroPage(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPage(cycles)
        self.LDX(value)
        return cycles

    def LDX_ZeroPageWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPageWithY(cycles)
        self.LDX(value)
        return cycles

    def LDX_AbsoluteWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithY(cycles)
        self.LDX(value)
        return cycles

    """  ========= STA Functions ========= """

    def STA_ZeroPage(self, cycles):
        self.PC += 1
        self.WriteZeroPage(cycles, self.A)

    def STA_ZeroPageWithX(self, cycles):
        self.PC += 1
        self.WriteZeroPageWithX(cycles, self.A)

    def STA_Absolute(self, cycles):
        self.PC += 1
        self.WriteAbsolute(cycles, self.A)

    def STA_AbsoluteWithX(self, cycles):
        self.PC += 1
        self.WriteAbsoluteWithX(cycles, self.A)

    def STA_AbsoluteWithY(self, cycles):
        self.PC += 1
        self.WriteAbsoluteWithY(cycles, self.A)

    def STA_IndirectWithX(self, cycles):
        self.PC += 1
        self.WriteIndirectWithX(cycles, self.A)

    def STA_IndirectWithY(self, cycles):
        self.PC += 1
        self.WriteIndirectWithY(cycles, self.A)

    """  ========= STX Functions ========= """

    def STX_ZeroPage(self, cycles):
        self.PC += 1
        self.WriteZeroPage(cycles, self.X)

    def STX_ZeroPageWithY(self, cycles):
        self.PC += 1
        self.WriteZeroPageWithY(cycles, self.X)

    def STX_Absolute(self, cycles):
        self.PC += 1
        self.WriteAbsolute(cycles, self.X)

    """  ========= STy Functions ========= """

    def STY_ZeroPage(self, cycles):
        self.PC += 1
        self.WriteZeroPage(cycles, self.Y)

    def STY_ZeroPageWithX(self, cycles):
        self.PC += 1
        self.WriteZeroPageWithX(cycles, self.Y)

    def STY_Absolute(self, cycles):
        self.PC += 1
        self.WriteAbsolute(cycles, self.Y)

    """  ========= Transfer Functions ========= """

    def TransfAccSetFlags(self, data):
        if data == 0:
            self.ZF = 1
        if data >= 0x80:
            self.NF = 1

    def TAX(self, cycles):
        self.PC += 1
        self.X = self.A
        self.TransfAccSetFlags(self.X)

    def TAY(self, cycles):
        self.PC += 1
        self.A = self.Y
        self.TransfAccSetFlags(self.Y)

    def TXA(self, cycles):
        self.PC += 1
        self.A = self.X
        self.TransfAccSetFlags(self.A)

    def TYA(self, cycles):
        self.PC += 1
        self.A = self.Y
        self.TransfAccSetFlags(self.A)

    """  ========= AND Functions ========= """
    # Do the basic function of AND
    def AND(self, cycles, value):
        result = self.A & value
        self.A = result
        if self.A == 0:
            self.ZF = 1
        self.NF = int(self.A >= 0x40)

    def AND_Immediate(self, cycles):
        self.PC += 1
        value, cycles = self.ReadImmediate(self.PC)
        self.AND(cycles, value)
        return cycles

    def AND_ZeroPage(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPage(self.PC)
        self.AND(cycles, value)
        return cycles

    def AND_ZeroPageWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPageWithX(cycles)
        self.AND(cycles, value)
        return cycles

    def AND_Absolute(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsolute(cycles)
        self.AND(cycles, value)
        return cycles

    def AND_AbsoluteWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithX(cycles)
        self.AND(cycles, value)
        return cycles

    def AND_AbsoluteWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithY(cycles)
        self.AND(cycles, value)
        return cycles

    def AND_IndirectWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadIndirectWithX(cycles)
        self.AND(cycles, value)
        return cycles

    def AND_IndirectWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadIndirectWithY(cycles)
        self.AND(cycles, value)
        return cycles

    """  ========= EOR Functions ========= """

    def EOR_Immediate(self, cycles):
        return False

    def EOR_ZeroPage(self, cycles):
        return False

    def EOR_ZeroPageWithX(self, cycles):
        return False

    def EOR_Absolute(self, cycles):
        return False

    def EOR_AbsoluteWithX(self, cycles):
        return False

    def EOR_AbsoluteWithY(self, cycles):
        return False

    def EOR_IndirectWithX(self, cycles):
        return False

    def EOR_IndirectWithY(self, cycles):
        return False

    """  ========= ORA Functions ========= """

    # Do the basic function of OR
    def OR(self, cycles, value):
        result = self.A | value
        self.A = result
        if self.A == 0:
            self.ZF = 1
        self.NF = int(self.A >= 0x40)

    def ORA_Immediate(self, cycles):
        self.PC += 1
        value, cycles = self.ReadImmediate(self.PC)
        self.OR(cycles, value)
        return cycles

    def ORA_ZeroPage(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPage(self.PC)
        self.OR(cycles, value)
        return cycles

    def ORA_ZeroPageWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPageWithX(cycles)
        self.OR(cycles, value)
        return cycles

    def ORA_Absolute(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsolute(cycles)
        self.OR(cycles, value)
        return cycles

    def ORA_AbsoluteWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithX(cycles)
        self.OR(cycles, value)
        return cycles

    def ORA_AbsoluteWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsoluteWithY(cycles)
        self.OR(cycles, value)
        return cycles

    def ORA_IndirectWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ReadIndirectWithX(cycles)
        self.OR(cycles, value)
        return cycles

    def ORA_IndirectWithY(self, cycles):
        self.PC += 1
        value, cycles = self.ReadIndirectWithY(cycles)
        self.OR(cycles, value)
        return cycles

    """  ========= BIT Functions ========= """

    def BIT(self, cycles, value):
        result = self.A & value
        if result == 0:
            self.ZF = 0
        bit_7 = (value & 0b10000000) >> 7
        self.NF = bit_7
        bit_6 = (value & 0b01000000) >> 6
        self.OF = bit_6

    def BIT_ZeroPage(self, cycles):
        self.PC += 1
        value, cycles = self.ReadZeroPage(self.PC)
        self.BIT(cycles, value)
        return cycles

    def BIT_Absolute(self, cycles):
        self.PC += 1
        value, cycles = self.ReadAbsolute(cycles)
        self.BIT(cycles, value)
        return cycles

    """
        Dictionary which allows us to lookup the various opcodes and call the
        associated function.
    """
    instructions = {
        0x00: NOP,
        0x01: ORA_IndirectWithX,
        0x03: NOP,
        0x04: NOP,
        0x05: ORA_ZeroPage,
        0x06: NOP,
        0x07: NOP,
        0x08: NOP,
        0x09: ORA_Immediate,
        0x0A: NOP,
        0x0B: NOP,
        0x0C: NOP,
        0x0D: ORA_Absolute,
        0x0E: NOP,
        0x0F: NOP,
        0x10: NOP,
        0x11: ORA_IndirectWithY,
        0x12: NOP,
        0x13: NOP,
        0x14: NOP,
        0x15: ORA_ZeroPageWithX,
        0x16: NOP,
        0x17: NOP,
        0x18: NOP,
        0x19: ORA_AbsoluteWithY,
        0x1A: NOP,
        0x1B: NOP,
        0x1C: NOP,
        0x1D: ORA_AbsoluteWithX,
        0x1E: NOP,
        0x1F: NOP,
        0x20: NOP,
        0x21: AND_IndirectWithX,
        0x22: NOP,
        0x23: NOP,
        0x24: BIT_ZeroPage,
        0x25: AND_ZeroPage,
        0x26: NOP,
        0x27: NOP,
        0x28: NOP,
        0x29: AND_Immediate,
        0x2A: NOP,
        0x2B: NOP,
        0x2C: BIT_Absolute,
        0x2D: AND_Absolute,
        0x2E: NOP,
        0x2F: NOP,
        0x30: NOP,
        0x31: AND_IndirectWithY,
        0x32: NOP,
        0x33: NOP,
        0x34: NOP,
        0x35: AND_ZeroPageWithX,
        0x36: NOP,
        0x37: NOP,
        0x38: NOP,
        0x39: AND_AbsoluteWithY,
        0x3A: NOP,
        0x3B: NOP,
        0x3C: NOP,
        0x3D: AND_AbsoluteWithX,
        0x3E: NOP,
        0x3F: NOP,
        0x40: NOP,
        0x41: EOR_IndirectWithX,
        0x42: NOP,
        0x43: NOP,
        0x44: NOP,
        0x45: EOR_ZeroPage,
        0x46: NOP,
        0x47: NOP,
        0x48: NOP,
        0x49: EOR_Immediate,
        0x4A: NOP,
        0x4B: NOP,
        0x4C: NOP,
        0x4D: EOR_Absolute,
        0x4E: NOP,
        0x4F: NOP,
        0x50: NOP,
        0x51: EOR_IndirectWithY,
        0x52: NOP,
        0x53: NOP,
        0x54: NOP,
        0x55: EOR_ZeroPageWithX,
        0x56: NOP,
        0x57: NOP,
        0x58: NOP,
        0x59: EOR_AbsoluteWithY,
        0x5A: NOP,
        0x5B: NOP,
        0x5C: NOP,
        0x5D: EOR_AbsoluteWithX,
        0x5E: NOP,
        0x5F: NOP,
        0x60: NOP,
        0x61: NOP,
        0x62: NOP,
        0x63: NOP,
        0x64: NOP,
        0x65: NOP,
        0x66: NOP,
        0x67: NOP,
        0x68: NOP,
        0x69: NOP,
        0x6A: NOP,
        0x6B: NOP,
        0x6C: NOP,
        0x6D: NOP,
        0x6E: NOP,
        0x6F: NOP,
        0x70: NOP,
        0x71: NOP,
        0x72: NOP,
        0x73: NOP,
        0x74: NOP,
        0x75: NOP,
        0x76: NOP,
        0x77: NOP,
        0x78: NOP,
        0x79: NOP,
        0x7A: NOP,
        0x7B: NOP,
        0x7C: NOP,
        0x7D: NOP,
        0x7E: NOP,
        0x7F: NOP,
        0x80: NOP,
        0x81: STA_IndirectWithX,
        0x82: NOP,
        0x83: NOP,
        0x84: STY_ZeroPage,
        0x85: STA_ZeroPage,
        0x86: STX_ZeroPage,
        0x87: NOP,
        0x88: NOP,
        0x89: NOP,
        0x8A: TXA,
        0x8B: NOP,
        0x8C: STY_Absolute,
        0x8D: STA_Absolute,
        0x8E: STX_Absolute,
        0x8F: NOP,
        0x90: NOP,
        0x91: STA_IndirectWithY,
        0x92: NOP,
        0x93: NOP,
        0x94: STY_ZeroPageWithX,
        0x95: STA_ZeroPageWithX,
        0x96: STX_ZeroPageWithY,
        0x97: NOP,
        0x98: TYA,
        0x99: STA_AbsoluteWithY,
        0x9A: NOP,
        0x9B: NOP,
        0x9C: NOP,
        0x9D: STA_AbsoluteWithX,
        0x9E: NOP,
        0x9F: NOP,
        0xA0: NOP,
        0xA1: NOP,
        0xA2: LDX_Immediate,
        0xA3: NOP,
        0xA4: NOP,
        0xA5: LDA_ZeroPage,
        0xA6: LDX_ZeroPage,
        0xA7: NOP,
        0xA8: TAY,
        0xA9: LDA_Immediate,
        0xAA: TAX,
        0xAB: NOP,
        0xAC: NOP,
        0xAD: LDA_Absolute,
        0xAE: LDX_Absolute,
        0xAF: NOP,
        0xB0: NOP,
        0xB1: LDA_IndirectWithY,
        0xB2: NOP,
        0xB3: NOP,
        0xB4: NOP,
        0xB5: LDA_ZeroPageWithX,
        0xB6: LDX_ZeroPageWithY,
        0xB7: NOP,
        0xB8: NOP,
        0xB9: LDA_AbsoluteWithY,
        0xBA: NOP,
        0xBB: NOP,
        0xBC: NOP,
        0xBD: LDA_AbsoluteWithX,
        0xBE: LDX_AbsoluteWithY,
        0xBF: NOP,
        0xC0: NOP,
        0xC1: NOP,
        0xC2: NOP,
        0xC3: NOP,
        0xC4: NOP,
        0xC5: NOP,
        0xC6: NOP,
        0xC7: NOP,
        0xC8: NOP,
        0xC9: NOP,
        0xCA: NOP,
        0xCB: NOP,
        0xCC: NOP,
        0xCD: NOP,
        0xCE: NOP,
        0xCF: NOP,
        0xD0: NOP,
        0xD1: NOP,
        0xD2: NOP,
        0xD3: NOP,
        0xD4: NOP,
        0xD5: NOP,
        0xD6: NOP,
        0xD7: NOP,
        0xD8: NOP,
        0xD9: NOP,
        0xDA: NOP,
        0xDB: NOP,
        0xDC: NOP,
        0xDD: NOP,
        0xDE: NOP,
        0xDF: NOP,
        0xE0: NOP,
        0xE1: NOP,
        0xE2: NOP,
        0xE3: NOP,
        0xE4: NOP,
        0xE5: NOP,
        0xE6: NOP,
        0xE7: NOP,
        0xE8: NOP,
        0xE9: NOP,
        0xEA: NOP,
        0xEB: NOP,
        0xEC: NOP,
        0xED: NOP,
        0xEE: NOP,
        0xEF: NOP,
        0xF0: NOP,
        0xF1: NOP,
        0xF2: NOP,
        0xF3: NOP,
        0xF4: NOP,
        0xF5: NOP,
        0xF6: NOP,
        0xF7: NOP,
        0xF8: NOP,
        0xF9: NOP,
        0xFA: NOP,
        0xFB: NOP,
        0xFC: NOP,
        0xFD: NOP,
        0xFE: NOP,
        0xFF: NOP,
    }
