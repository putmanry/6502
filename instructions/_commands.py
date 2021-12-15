"""
All the processor instructions
"""
import logging

from instructions._adc import ADC
from instructions._and import AND
from instructions._bit import BIT
from instructions._cmp import CMP
from instructions._eor import EOR
from instructions._lda import LDA
from instructions._ldx import LDX
from instructions._ora import ORA
from instructions._sbc import SBC
from instructions._sta import STA
from instructions._stx import STX
from instructions._sty import STY
from instructions._transfer import Transfer


class Commands:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.opcodes = {}

    def NOP(self, cycles):
        self.log.info("NOP Not implemented")
        return cycles

    def commands_initialize(self):
        self.log.debug("Commands init")

        self.opcode_adc = ADC()
        self.opcodes.update(ADC.register_opcodes(self.opcode_adc))
        self.opcode_adc = AND()
        self.opcodes.update(AND.register_opcodes(self.opcode_adc))
        self.opcode_lda = BIT()
        self.opcodes.update(BIT.register_opcodes(self.opcode_lda))
        self.opcode_lda = CMP()
        self.opcodes.update(CMP.register_opcodes(self.opcode_lda))
        self.opcode_lda = EOR()
        self.opcodes.update(EOR.register_opcodes(self.opcode_lda))
        self.opcode_lda = LDA()
        self.opcodes.update(LDA.register_opcodes(self.opcode_lda))
        self.opcode_lda = LDX()
        self.opcodes.update(LDX.register_opcodes(self.opcode_lda))
        self.opcode_lda = ORA()
        self.opcodes.update(ORA.register_opcodes(self.opcode_lda))
        self.opcode_lda = SBC()
        self.opcodes.update(SBC.register_opcodes(self.opcode_lda))
        self.opcode_lda = STA()
        self.opcodes.update(STA.register_opcodes(self.opcode_lda))
        self.opcode_lda = STX()
        self.opcodes.update(STX.register_opcodes(self.opcode_lda))
        self.opcode_lda = STY()
        self.opcodes.update(STY.register_opcodes(self.opcode_lda))
        self.opcode_lda = Transfer()
        self.opcodes.update(Transfer.register_opcodes(self.opcode_lda))
