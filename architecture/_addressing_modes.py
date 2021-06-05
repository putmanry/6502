"""
Addressing modes for the CPU
"""


class _AddressingModesMixin:
    def Absolute(self, cycles):
        """
        The second and the third bytes of the instruction specify the memory
        address where data is located
        """
        print("Absolute addressing mode")
        # TODO: This is wrong, fix it. Looks more like Immediate mode
        value = self.read_word(self.PC + 1)
        self.PC = self.PC + 1
        cycles = cycles - 1
        return value, cycles

    def Immediate(self, cycles):
        """
        8 bit data is provided as the second byte in the instruction
        """
        print("Immediate Adderssing mode")
        cycles = cycles - 1
        value = self.read_mem(self.PC + 1)
        return value, cycles

    def ZeroPage(self, cycles):
        """
        The second byte in the instruction points to location in page
        zero (0000h - 00ffh) where data is stored
        """
        print("Zero Page Addressing Mode")
        value = self.read_mem(self.PC + 1)
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
        print("Zero Page Addressing Mode")
        value = self.read_mem(self.PC + 1)
        if value >= 0x00 and value <= 0xFF:
            cycles = cycles - 2
            value = self.read_mem(value)
        else:
            print("error zero page address out of bounds")
        return value, cycles
