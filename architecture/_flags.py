"""
Processor flags and associated functions
"""


class _FlagsMixin:
    def __init__(self):
        self.CF = 0  # Carry Flag Bit
        self.ZF = 0  # Zero Flag Bit
        self.ID = 0  # Interrupt Disable
        self.DM = 0  # Decimal mode
        self.BC = 0  # Break Command
        self.OF = 0  # Overflow Command
        self.NF = 0  # Negative Flag

    def __str__(self):
        print("CF: {}      ZF: {}".format(self.CF, self.ZF))
        print("ID: {}      DM: {}".format(self.ID, self.DM))
        print("BC: {}      OF: {}".format(self.BC, self.OF))
        print("NF: {}".format(self.NF))

    def flags_reset(self):
        self.CF = 0  # Carry Flag Bit
        self.ZF = 0  # Zero Flag Bit
        self.ID = 0  # Interrupt Disable
        self.DM = 0  # Decimal mode
        self.BC = 0  # Break Command
        self.OF = 0  # Overflow Command
        self.NF = 0  # Negative Flag


"""
TODO: Add in getter/setter for the vars
"""
