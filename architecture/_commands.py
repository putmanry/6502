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
        value, cycles = self.ZeroPage(cycles)
        self.LDA(value)
        return cycles

    # Handles LDA with Immediate load
    def LDA_Immediate(self, cycles):
        self.PC += 1
        value, cycles = self.Immediate(cycles)
        self.LDA(value)
        return cycles

    def LDA_ZeroPageWithX(self, cycles):
        self.PC += 1
        value, cycles = self.ZeroPageWithX(cycles)
        self.LDA(value)
        return cycles

    def LDA_Absolute(self, cycles):
        self.PC += 1
        value, cycles = self.Absolute(cycles)
        self.LDA(value)
        return cycles

    def LDA_AbsoluteWithX(self, cycles):
        self.PC += 1
        value, cycles = self.AbsoluteWithX(cycles)
        self.LDA(value)
        return cycles

    def LDA_AbsoluteWithY(self, cycles):
        self.PC += 1
        value, cycles = self.AbsoluteWithY(cycles)
        self.LDA(value)
        return cycles

    def LDA_IndirectWithX(self, cycles):
        self.PC += 1
        value, cycles = self.IndirectWithX(cycles)
        self.LDA(value)
        return cycles

    def LDA_IndirectWithY(self, cycles):
        self.PC += 1
        value, cycles = self.IndirectWithY(cycles)
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
        value, cycles = self.Immediate(cycles)
        self.LDX(value)
        return cycles

    def LDX_Absolute(self, cycles):
        return True

    def LDX_ZeroPage(self, cycles):
        return True

    def LDX_ZeroPageY(self, cycles):
        return True

    def LDX_AbsoluteWithY(self, cycles):
        return True

    """
        Dictionary which allows us to lookup the various opcodes and call the
        associated function.
    """
    instructions = {
        0x00: NOP,
        0x01: NOP,
        0x03: NOP,
        0x04: NOP,
        0x05: NOP,
        0x06: NOP,
        0x07: NOP,
        0x08: NOP,
        0x09: NOP,
        0x0A: NOP,
        0x0B: NOP,
        0x0C: NOP,
        0x0D: NOP,
        0x0E: NOP,
        0x0F: NOP,
        0x10: NOP,
        0x11: NOP,
        0x12: NOP,
        0x13: NOP,
        0x14: NOP,
        0x15: NOP,
        0x16: NOP,
        0x17: NOP,
        0x18: NOP,
        0x19: NOP,
        0x1A: NOP,
        0x1B: NOP,
        0x1C: NOP,
        0x1D: NOP,
        0x1E: NOP,
        0x1F: NOP,
        0x20: NOP,
        0x21: NOP,
        0x22: NOP,
        0x23: NOP,
        0x24: NOP,
        0x25: NOP,
        0x26: NOP,
        0x27: NOP,
        0x28: NOP,
        0x29: NOP,
        0x2A: NOP,
        0x2B: NOP,
        0x2C: NOP,
        0x2D: NOP,
        0x2E: NOP,
        0x2F: NOP,
        0x30: NOP,
        0x31: NOP,
        0x32: NOP,
        0x33: NOP,
        0x34: NOP,
        0x35: NOP,
        0x36: NOP,
        0x37: NOP,
        0x38: NOP,
        0x39: NOP,
        0x3A: NOP,
        0x3B: NOP,
        0x3C: NOP,
        0x3D: NOP,
        0x3E: NOP,
        0x3F: NOP,
        0x40: NOP,
        0x41: NOP,
        0x42: NOP,
        0x43: NOP,
        0x44: NOP,
        0x45: NOP,
        0x46: NOP,
        0x47: NOP,
        0x48: NOP,
        0x49: NOP,
        0x4A: NOP,
        0x4B: NOP,
        0x4C: NOP,
        0x4D: NOP,
        0x4E: NOP,
        0x4F: NOP,
        0x50: NOP,
        0x51: NOP,
        0x52: NOP,
        0x53: NOP,
        0x54: NOP,
        0x55: NOP,
        0x56: NOP,
        0x57: NOP,
        0x58: NOP,
        0x59: NOP,
        0x5A: NOP,
        0x5B: NOP,
        0x5C: NOP,
        0x5D: NOP,
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
        0x81: NOP,
        0x82: NOP,
        0x83: NOP,
        0x84: NOP,
        0x85: NOP,
        0x86: NOP,
        0x87: NOP,
        0x88: NOP,
        0x89: NOP,
        0x8A: NOP,
        0x8B: NOP,
        0x8C: NOP,
        0x8D: NOP,
        0x8E: NOP,
        0x8F: NOP,
        0x90: NOP,
        0x91: NOP,
        0x92: NOP,
        0x93: NOP,
        0x94: NOP,
        0x95: NOP,
        0x96: NOP,
        0x97: NOP,
        0x98: NOP,
        0x99: NOP,
        0x9A: NOP,
        0x9B: NOP,
        0x9C: NOP,
        0x9D: NOP,
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
        0xA8: NOP,
        0xA9: LDA_Immediate,
        0xAA: NOP,
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
        0xB6: LDX_ZeroPageY,
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
