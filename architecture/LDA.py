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
