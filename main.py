from architecture.processor import CPU_6502


def main():

    processor = CPU_6502()
    processor.reset()
    processor.__str__()
    var = processor.execute(2)


if __name__ == "__main__":
    main()
