from architecture.processor import CPU_6502
import datetime


class _BaseInstruction:
    def setUp(self) -> None:
        print("\n*************** New Test Run ****************")
        ct = datetime.datetime.now()
        print("timestamp: ", ct)
        self.processor = CPU_6502()
        self.processor.reset()
        # self.processor.__str__()
        return super().setUp()

    def tearDown(self) -> None:
        del self.processor
        return super().tearDown()

    def checkRegisters(self, CPUCopy, ZFCopy=0, NFCopy=0):
        self.assertEqual(CPUCopy.CF, self.processor.CF, "CF not the same")
        self.assertEqual(CPUCopy.ID, self.processor.ID, "ID not the same")
        self.assertEqual(CPUCopy.DM, self.processor.DM, "DM not the same")
        self.assertEqual(CPUCopy.BC, self.processor.BC, "BC not the same")
        self.assertEqual(CPUCopy.OF, self.processor.OF, "OF not the same")

        self.assertEqual(self.processor.ZF, ZFCopy, "ZF not set correctly")
        self.assertEqual(self.processor.NF, NFCopy, "NF not set correctly")

    def programSetup(self, instructions):
        self.processor.reset()
        # Inline program to test with
        for i in range(len(instructions)):
            self.processor.memory[instructions[i][0]] = instructions[i][1]
