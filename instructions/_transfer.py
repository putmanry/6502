"""  ========= Transfer Functions ========= """
import logging


class Transfer:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("Transfer Init")
        pass

    def register_opcodes(self):
        self.log.debug("Transfer Register opcodes")
        return {0xAA: self.TAX, 0xA8: self.TAY, 0x8A: self.TXA, 0x98: self.TYA}

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
