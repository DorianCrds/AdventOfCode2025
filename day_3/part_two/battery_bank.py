class BatteryBank:
    def __init__(self, line: str):
        self.line_list: list[int] = list(map(int, line.strip()))

        self.remaining_slots = 12
        self.values_list = []
        self.result = ""

        self.init_process()

    def init_process(self):
        while self.remaining_slots > 0:
            self.process_line()

        if len(self.values_list) == 12:
            for value in self.values_list:
                self.result += str(value)

    def process_line(self):
        found_digit = False
        value = 9
        temporary_slice = []
        while not found_digit:
            if value < 1:
                print("Values not found")

            for i in range(len(self.line_list)):
                digit = self.line_list[i]
                temporary_slice = self.line_list[i + 1:]
                if digit == value and len(temporary_slice) >= self.remaining_slots - 1:
                    self.values_list.append(digit)
                    self.remaining_slots -= 1
                    found_digit = True
                    print("-" * 10)
                    print("Slice lenght : ", len(temporary_slice))
                    print("Result list : ", self.values_list)
                    print("Remaining slots : ", self.remaining_slots)
                    print("Sliced line : ", temporary_slice)
                    break

            if found_digit:
                self.line_list = temporary_slice

            value -= 1