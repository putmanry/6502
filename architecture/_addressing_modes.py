"""
Addressing modes for the CPU
"""


class _AddressingModesMixin:
    # =========== Mem read commands ==================

    def ReadAbsolute(self, cycles):
        """
        The second and the third bytes of the instruction specify the memory
        address where data is located
        """
        # print("Absolute addressing mode")

        hi_byte = self.read_mem(self.PC)
        self.PC += 1
        lo_byte = self.read_mem(self.PC)
        self.PC += 1
        location = (lo_byte << 8) | hi_byte
        value = self.read_mem(location)
        cycles = cycles - 1
        return value, cycles

    def ReadImmediate(self, cycles):
        """
        8 bit data is provided as the second byte in the instruction
        """
        # print("Immediate Adderssing mode")
        cycles = cycles - 1
        value = self.read_mem(self.PC)
        return value, cycles

    def ReadZeroPage(self, cycles):
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

    def ReadZeroPageWithX(self, cycles):
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
        # print("Zero Page with X Addressing Mode")
        # TODO: Fix memaddress wrap around
        value = self.read_mem(self.PC)
        location = value + self.X
        """
        print(
            "Val: 0x{:04x}      X: 0x{:04x}    location: 0x{:04}".format(
                self.PC, self.x, location
            )
        )"""
        cycles = cycles - 3
        value2 = self.read_mem(location)
        return value2, cycles

    def ReadAbsoluteWithX(self, cycles):
        """
        The address to be accessed by an instruction using X register indexed
        absolute addressing is computed by taking the 16 bit address from
        the instruction and added the contents of the X register. For example
        if X contains $92 then an STA $2000,X instruction will store the
        accumulator at $2092 (e.g. $2000 + $92).
        """
        # print("AbsoluteWithX Addressing Mode")
        hi_byte = self.read_mem(self.PC)
        self.PC += 1
        lo_byte = self.read_mem(self.PC)
        self.PC += 1
        location = (lo_byte << 8) | hi_byte
        location = location + self.X
        cycles = cycles - 3
        value2 = self.read_mem(location)
        return value2, cycles

    def ReadAbsoluteWithY(self, cycles):
        """
        The address to be accessed by an instruction using Y register indexed
        absolute addressing is computed by taking the 16 bit address from
        the instruction and added the contents of the Y register. For example
        if Y contains $92 then an STA $2000,Y instruction will store the
        accumulator at $2092 (e.g. $2000 + $92).
        """
        # print("AbsoluteWithY Addressing Mode")
        hi_byte = self.read_mem(self.PC)
        self.PC += 1
        lo_byte = self.read_mem(self.PC)
        self.PC += 1
        location = (lo_byte << 8) | hi_byte
        location = location + self.Y
        cycles = cycles - 3
        value2 = self.read_mem(location)
        return value2, cycles

    def ReadIndirectWithX(self, cycles):
        """The vector is chosen by adding the value in the X index register
        to the given zero page address. The resulting zero page address is the
        vector from which the effective address is read.

        Indexed-indirect addressing is written as follows:

        LDX #$04
        LDA ($02,X)
        In the above case, X is loaded with four (4), so the vector is calculated as $02
        plus four (4). The resulting vector is ($06). If zero page memory $06 contains 00 80,
        then the effective address from the vector (06) would be $8000.
        """

        """ Another example:
        This mode is only used with the X register. Consider a situation where the instruction is 
        LDA ($20,X), X contains $04, and memory at $24 contains 0024: 74 20, First, X is added 
        to $20 to get $24. The target address will be fetched from $24 resulting in a target 
        address of $2074. Register A will be loaded with the contents of memory at $2074.

        If X + the immediate byte will wrap around to a zero-page address. So you could code 
        that like targetAddress = (X + opcode[1]) & 0xFF . """

        # TODO: Handle Zero Page Wrap around
        # print("IndirectWithX Addressing Mode")
        value = self.read_mem(self.PC)  # gives us the 0x02
        location = self.X + value  # gives the 0x02 + 0x04
        value2 = self.read_word(location)  # read from 0x06 to get the 0x0080
        return value2, cycles

    def ReadIndirectWithY(self, cycles):
        # see also: https://slark.me/c64-downloads/6502-addressing-modes.pdf

        """
        This mode is only used with the Y register. It differs in the
        order that Y is applied to the indirectly fetched address. An example
        instruction that uses indirect index addressing is LDA ($86),Y . To calculate
        the target address, the CPU will first fetch the address stored at zero page
        location $86. That address will be added to register Y to get the final target
        address. For LDA ($86),Y, if the address stored at $86 is $4028
        (memory is 0086: 28 40, remember little endian) and register Y contains $10,
        then the final target address would be $4038. Register A will be loaded with
        the contents of memory at $4038.

        Indirect indirect addressing is the most common indirection mode used on
        the 6502. In instruction contains the zero page location of the least
        significant byte of 16 bit address. The Y register is dynamically added
        to this value to generated the actual target address for operation.
        """
        # The operand  $AA is a zero page address, the contents of $AA are added with carry (C)
        # to the Y register
        #      $AA + Y (C) the results containts the lo_byte of the EA
        # The content of address $AA + $01 + C contain the MSB of the EA
        # if Y = $E9 and
        # if $A4 contains $51 and
        # if $A5 contains $3F then:
        # LDA ($A4), Y results in
        # $AA + Y (C) => ($51 + $E9) (C) => $13A (C) => $3A -> EA LSB and
        # $AA + $01 (C) -> ($3F + C) => ($3F + $01) => $40 -> EA MSB
        #                                                   $403A EA
        # print("IndirectWithY Addressing Mode")
        value = self.read_mem(self.PC)  # fetch zero page location $A4 which is $51
        value2 = self.read_mem(value)
        lo_byte = value2 + self.Y  # $13A
        if lo_byte > 0xFF:  # this means we had a carry
            lo_byte = lo_byte - 0x100
            hi_byte = self.read_mem(value + 1) + 1
        else:  # we didn't have a carry
            hi_byte = self.read_mem(value + 1)
        location = hi_byte << 8 | lo_byte
        value3 = self.read_mem(location)

        return value3, cycles

    def ReadZeroPageWithY(self, cycles):
        """
        The address to be accessed by an instruction using indexed zero page
        addressing is calculated by taking the 8 bit zero page address from
        the instruction and adding the current value of the Y register to it.
        This mode can only be used with the LDX and STX instructions.
        """
        value = self.read_mem(self.PC)
        value2 = value + self.Y
        value3 = self.read_mem(value2)
        return value3, cycles

    # =========== Mem write commands ==================

    def WriteAbsolute(self, cycles, data):
        """
        The second and the third bytes of the instruction specify the memory
        address where data is located
        """
        # print("Absolute addressing mode")

        hi_byte = self.read_mem(self.PC)
        self.PC += 1
        lo_byte = self.read_mem(self.PC)
        self.PC += 1
        location = (lo_byte << 8) | hi_byte
        self.write_word(location, data)
        cycles = cycles - 1
        return cycles

    def WriteImmediate(self, cycles):
        """
        8 bit data is provided as the second byte in the instruction
        """
        # print("Immediate Adderssing mode")
        cycles = cycles - 1
        value = self.read_mem(self.PC)
        return value, cycles

    def WriteZeroPage(self, cycles, data):
        """
        The second byte in the instruction points to location in page
        zero (0x00 - 0xFF) where data is stored
        """
        # print("Zero Page Addressing Mode")
        value = self.read_mem(self.PC)
        if value >= 0x00 and value <= 0xFF:
            cycles = cycles - 2
            self.write_mem(value, data)
        else:
            print("error zero page address out of bounds")
        return cycles

    def WriteZeroPageWithX(self, cycles, data):
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
        # print("Zero Page with X Addressing Mode")
        # TODO: Fix memaddress wrap around
        value = self.read_mem(self.PC)
        location = value + self.X
        """
        print(
            "Val: 0x{:04x}      X: 0x{:04x}    location: 0x{:04}".format(
                self.PC, self.x, location
            )
        )"""
        self.write_mem(location, data)
        cycles = cycles - 3
        return cycles

    def WriteAbsoluteWithX(self, cycles, data):
        """
        The address to be accessed by an instruction using X register indexed
        absolute addressing is computed by taking the 16 bit address from
        the instruction and added the contents of the X register. For example
        if X contains $92 then an STA $2000,X instruction will store the
        accumulator at $2092 (e.g. $2000 + $92).
        """
        # print("AbsoluteWithX Addressing Mode")
        hi_byte = self.read_mem(self.PC)
        self.PC += 1
        lo_byte = self.read_mem(self.PC)
        self.PC += 1
        location = (lo_byte << 8) | hi_byte
        location = location + self.X
        cycles = cycles - 3
        self.write_mem(location, data)
        return cycles

    def WriteAbsoluteWithY(self, cycles, data):
        """
        The address to be accessed by an instruction using Y register indexed
        absolute addressing is computed by taking the 16 bit address from
        the instruction and added the contents of the Y register. For example
        if X contains $92 then an STA $2000,Y instruction will store the
        accumulator at $2092 (e.g. $2000 + $92).
        """
        # print("AbsoluteWithY Addressing Mode")
        hi_byte = self.read_mem(self.PC)
        self.PC += 1
        lo_byte = self.read_mem(self.PC)
        self.PC += 1
        location = (lo_byte << 8) | hi_byte
        location = location + self.Y
        cycles = cycles - 3
        self.write_mem(location, data)
        return cycles

    def WriteIndirectWithX(self, cycles, data):
        """The vector is chosen by adding the value in the X index register
        to the given zero page address. The resulting zero page address is the
        vector from which the effective address is read.

        Indexed-indirect addressing is written as follows:

        LDX #$04
        LDA ($02,X)
        In the above case, X is loaded with four (4), so the vector is calculated as $02
        plus four (4). The resulting vector is ($06). If zero page memory $06 contains 00 80,
        then the effective address from the vector (06) would be $8000.
        """

        """ Another example:
        This mode is only used with the X register. Consider a situation where the instruction is 
        LDA ($20,X), X contains $04, and memory at $24 contains 0024: 74 20, First, X is added 
        to $20 to get $24. The target address will be fetched from $24 resulting in a target 
        address of $2074. Register A will be loaded with the contents of memory at $2074.

        If X + the immediate byte will wrap around to a zero-page address. So you could code 
        that like targetAddress = (X + opcode[1]) & 0xFF . """

        # TODO: Handle Zero Page Wrap around
        print("IndirectWithX Addressing Mode")
        value = self.read_mem(self.PC)
        location = self.X + value
        self.write_mem(location, data)
        return cycles

    def WriteIndirectWithY(self, cycles, data):
        # see also: https://slark.me/c64-downloads/6502-addressing-modes.pdf

        """
        This mode is only used with the Y register. It differs in the
        order that Y is applied to the indirectly fetched address. An example
        instruction that uses indirect index addressing is LDA ($86),Y . To calculate
        the target address, the CPU will first fetch the address stored at zero page
        location $86. That address will be added to register Y to get the final target
        address. For LDA ($86),Y, if the address stored at $86 is $4028
        (memory is 0086: 28 40, remember little endian) and register Y contains $10,
        then the final target address would be $4038. Register A will be loaded with
        the contents of memory at $4038.

        Indirect indirect addressing is the most common indirection mode used on
        the 6502. In instruction contains the zero page location of the least
        significant byte of 16 bit address. The Y register is dynamically added
        to this value to generated the actual target address for operation.
        """
        # The operand  $AA is a zero page address, the contents of $AA are added with carry (C)
        # to the Y register
        #      $AA + Y (C) the results containts the LSB of the EA
        # The content of address $AA + $01 + C contain the MSB of the EA
        # if Y = $E9 and
        # if $A4 contains $51 and
        # if $A5 contains $3F then:
        # LDA ($A4), Y results in
        # $AA + Y (C) => ($51 + $E9) (C) => $13A (C) => $3A -> EA LSB and
        # $AA + $01 (C) -> ($3F + C) => ($3F + $01) => $40 -> EA MSB
        #                                                   $403A EA
        # print("IndirectWithY Addressing Mode")
        value = self.read_mem(self.PC)  # fetch zero page location $A4 which is $51
        value2 = self.read_mem(value)
        lo_byte = value2 + self.Y  # $13A
        if lo_byte > 0xFF:  # this means we had a carry
            lo_byte = lo_byte - 0x100
            hi_byte = self.read_mem(value + 1) + 1
        else:  # we didn't have a carry
            hi_byte = self.read_mem(value + 1)
        location = hi_byte << 8 | lo_byte
        self.write_mem(location, data)

        return cycles

    def WriteZeroPageWithY(self, cycles, data):
        """
        The address to be accessed by an instruction using indexed zero page
        addressing is calculated by taking the 8 bit zero page address from
        the instruction and adding the current value of the Y register to it.
        This mode can only be used with the LDX and STX instructions.
        """
        value = self.read_mem(self.PC)
        value2 = value + self.Y
        self.write_mem(value2, data)
        return cycles
