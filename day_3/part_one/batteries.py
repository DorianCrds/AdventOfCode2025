class Batterie:
    def __init__(self, line: str):
        self.digit_list = list(line.strip())
        self.length = len(self.digit_list)
        self.first_max_value = 0
        self.second_max_value = 0
        self.max_value_number = 0

        self.find_max_values()

    def find_max_values(self):
        self.first_max_value = max(self.digit_list[:-1])
        print("First max : ", self.first_max_value)
        index_to_cut = self.digit_list.index(self.first_max_value) + 1
        print(f"index to cut : {index_to_cut}")
        self.second_max_value = max(self.digit_list[index_to_cut:])
        print("Second max : ", self.second_max_value)

        max_value_as_str = str(self.first_max_value) + str(self.second_max_value)
        print("max value as str : ", max_value_as_str)
        self.max_value_number = int(max_value_as_str)
        print("Max value int : ", self.max_value_number)
