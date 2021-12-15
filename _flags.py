"""
Processor flags and associated functions
"""
from dataclasses import dataclass
import logging


@dataclass
class Flags:
    CF: int = 0  # Carry Flag Bit
    ZF: int = 0  # Zero Flag Bit
    ID: int = 0  # Interrupt Disable
    DM: int = 0  # Decimal mode
    BC: int = 0  # Break Command
    OF: int = 0  # Overflow Command
    NF: int = 0  # Negative Flag

    def flags_reset(self):

        self.log = logging.getLogger(__name__)
        self.log.debug("flags reset")
        self.CF = 0  # Carry Flag Bit
        self.ZF = 0  # Zero Flag Bit
        self.ID = 0  # Interrupt Disable
        self.DM = 0  # Decimal mode
        self.BC = 0  # Break Command
        self.OF = 0  # Overflow Command
        self.NF = 0  # Negative Flag
