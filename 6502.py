'''
6502 CPU Emulator
Using data here: http://www.obelisk.me.uk/index.html
'''

class 6502:
    int PC 'Program counter
    int SP 'Stack pointer'
    int Acc 'Accumulator'
    int x   'X register'
    int y   'Y register'
    int Status 'Processor Status'

    CF 1<<7 'Carry Flag Bit'
    ZF 1<<6 'Zero Flag Bit'
    ID 1<<5 'Interrupt Disable'
    DM 1<<4 'Decimal mode'
    BC 1<<3 'Break Command'
    OF 1<<2 'Overflow Command'
    NF 1<<1 'Negative Flag'
