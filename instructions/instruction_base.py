from abc import ABC, abstractmethod


class Instruction(ABC):
    def __init__():
        pass

    @abstractmethod
    def base_operation(value: int) -> int:
        # Takes in the value to operate on
        # Returns the number of cycles that were consumed
        pass

    @abstractmethod
    def register_opcodes() -> dict:
        """Returns the hex level commands that are supported by this opcode
        Used to look up which command to run
        """
        pass

    @abstractmethod
    def MemAccess_ZeroPage(value: int) -> int:
        pass

    @abstractmethod
    def MemAccess_Immediate(value: int) -> int:
        pass

    @abstractmethod
    def MemAccess_ZeroPageWithX(value: int) -> int:
        pass

    @abstractmethod
    def MemAccess_Absolute(value: int) -> int:
        pass

    @abstractmethod
    def MemAccess_AbsoluteWithX(value: int) -> int:
        pass

    @abstractmethod
    def MemAccess_AbsoluteWithY(value: int) -> int:
        pass

    @abstractmethod
    def MemAccess_IndirectWithX(value: int) -> int:
        pass

    @abstractmethod
    def MemAccess_IndirectWithY(value: int) -> int:
        pass
