'''
Memory structure
'''


class _MemoryMixin:
    memory = [65536]

    def read_mem(self, location):
        print("read mem")
        return self.memory[location]

    def write_mem(self, location, value):
        return True
