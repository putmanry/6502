"""
Addressing modes for the CPU
"""


class _AddressingModesMixin:
    def Absolute(self, cycles):
        """
        The second and the third bytes of the instruction specify the memory
        address where data is located
        """
        # print("Absolute addressing mode")

        hi_byte = self.read_mem(self.PC)
        self.PC += 1
        lo_byte = self.read_mem(self.PC)
        self.PC += 1
        loc = (lo_byte << 8) | hi_byte
        value = self.read_mem(loc)
        cycles = cycles - 1
        return value, cycles

    def Immediate(self, cycles):
        """
        8 bit data is provided as the second byte in the instruction
        """
        # print("Immediate Adderssing mode")
        cycles = cycles - 1
        value = self.read_mem(self.PC)
        return value, cycles

    def ZeroPage(self, cycles):
        """
        The second byte in the instruction points to location in page
        zero (0x00 - 0xFF) where data is stored
        """
        # print("Zero Page Addressing Mode")
        value = self.read_mem(self.PC)
        if value >= 0x00 and value <= 0xFF:
            cycles = cycles - 2
            value = self.read_mem(value)
        else:
            print("error zero page address out of bounds")
        return value, cycles

    def ZeroPageWithX(self, cycles):
        """
        The address to be accessed by an instruction using indexed zero
        page addressing is calculated by taking the 8 bit zero page address
        from the instruction and adding the current value of the X register
        to it. For example if the X register contains $0F and the instruction
        LDA $80,X is executed then the accumulator will be loaded from $008F
        (e.g. $80 + $0F => $8F).

        NB:
        The address calculation wraps around if the sum of the base address
        and the register exceed $FF. If we repeat the last example but with $FF
        in the X register then the accumulator will be loaded from $007F
        (e.g. $80 + $FF => $7F) and not $017F.
        """
        print("Zero Page with X Addressing Mode")
        value = self.read_mem(self.PC)
        loc = value + self.X
        """
        print(
            "Val: 0x{:04x}      X: 0x{:04x}    loc: 0x{:04}".format(
                self.PC, self.x, loc
            )
        )"""
        cycles = cycles - 3
        value2 = self.read_mem(loc)
        return value2, cycles
