"""
Memory Class
"""
import logging

MAX_MEM = 1024 * 64


class Memory:
    def __init__(self):
        self.memory = [0] * MAX_MEM
        self.log = logging.getLogger(__name__)

    def mem_intialize(self):
        self.log.debug("Memory init")
        return True

    def read_mem(self, location):
        if location >= 0 and location <= MAX_MEM:
            self.log.debug("read mem location 0x{:04x}".format(location))
            return self.memory[location]

    def write_mem(self, location, value):
        print("write mem location 0x{:04x} data 0x{:04x}".format(location, value))
        self.memory[location] = value

    def read_word(self, location):
        if location >= 0 and location <= MAX_MEM:
            self.log.debug("read word location", location)
            loc_lo = self.memory[location]
            loc_hi = self.memory[location + 1]
            value = loc_hi << 8 | loc_lo
        return self.memory[value]

    def read_word_address(self, location):
        self.log.debug("read word address {location}")
        if location >= 0 and location <= MAX_MEM:
            return self.memory[location]

    def write_word(self, location, value):
        self.log.debug(
            "write mem location 0x{:04x} data 0x{:04x}".format(location, value)
        )
        self.memory[location] = value
