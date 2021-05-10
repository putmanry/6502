from architecture.processor import CPU_6502


def main():

    processor = CPU_6502()
    print("Hellow World")
    print(processor)
    processor.Absolute()
    var = processor.read_mem(0)
    print(var)
   
       
if __name__ == "__main__":
    main()
