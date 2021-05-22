"""
Addressing modes for the CPU
"""


class _AddressingModesMixin:
    def Implied():
        """
        The data value/data adress is implicity associted with the instruction.
        """
        return True

    def Accumulator():
        """
        The instruction implies that the data is in the accumulator
        """
        return True

    def Absolute(self):
        """
        Teh second and the third bytes of the instruction specify the memory address where data is located
        """
        print("Absolute addressing mode")
        return True

    def Immediate():
        """
        8 bit data is provided as the second bte in the instruction
        """
        return True

    def ZeroPage():
        """
        The second byte in the instruction points to lcation in page zero (0000h - 00ffh) where data is stored
        """
        return True

    def IndexedZeroPage():
        """
        the contents of the X or Y register is added to the second byte of the instruction (carry is ignored),
        and the resulting byte is a memory offset in page zero (0000h - 00FFh) where data is located. This form of
        addressing is written as "addr8, X" or "addr8, Y", where addr8 is an 8-bit value.
        """
        return True

    def IndexedAbsolute():
        """
        the contents of the X or Y register is added to the 16-bit pointer specified in the second and third
        bytes of the instruction, and the resulting 16-bit value is a pointer to memory where data is located.
        This form of addressing is written as "addr16, X" or "addr16, Y", where addr16 is a 16-bit value.
        """
        return True

    def Relateive():
        """
        one byte offset is added to the contents of the program counter register. The offset is a signed number
        in the range -127 - +128.
        """
        return True

    def IndexedDirect():
        """
        the contents of the X register is added to the second byte provided in the instruction (carry is ignored),
        the resulting byte is a memory offset in page zero where a 16-bit pointer is stored. The 16-pointer points to data.
        This type of addressing is written as "(addr8, X)", where addr8 is an 8-bit value. This addressing is useful for
        addressing an array of data pointers.
        """
        return True

    def IndirectIndexed():
        """
        the second byte in the instruction points to memory in page zero where 16-bit data pointer is stored.
        This pointer is added to the contents of the Y register, the resulting 16-bit value is an offset to memory where
        data is located. This type of addressing is written as "(addr8), Y", where addr8 is an 8-bit value.
        """
        return True

    def AbsoluteIndirect():
        """
        The second and third bytes in the instruction specify the memory address containing 16-bit data, which is loaded
        into the program counter. This type of addressing is written as "(addr16)", where addr16 is a 16-bit value.
        """
        return True
