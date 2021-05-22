import architecture.processor as proc


def test_1():
    assert proc.CPU_6502.execute(1, 1)
