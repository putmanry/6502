from architecture.processor import CPU_6502


def main():

    processor = CPU_6502()
    processor.reset()
    var = processor.execute(5)
    print(var)


if __name__ == "__main__":
    main()
