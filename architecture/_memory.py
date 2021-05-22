"""
Memory structure
"""

MAX_MEM = 1024 * 64


class _MemoryMixin:
    memory = [0] * MAX_MEM

    def mem_intialize(self):
        print("mem init")
        return True

    def read_mem(self, location):
        if location >= 0 and location <= MAX_MEM:
            print("read mem location", location)
            return self.memory[location]

    def write_mem(self, location, value):
        return True
