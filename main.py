from processor import CPU_6502
import logging

log_format = "[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s"


def main():
    logger = logging.getLogger("my_logger")
    # Define basic configuration
    logging.basicConfig(
        # Define logging level
        level=logging.DEBUG,
        # Define the format of log messages
        format=log_format,
        # Declare handlers
        handlers=[logging.StreamHandler()],
    )

    processor = CPU_6502()
    processor.reset()
    processor.__str__()
    # var = processor.execute(2)


if __name__ == "__main__":
    main()
