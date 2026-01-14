class Problem:
    def __init__(self, values: list[int], op: str):
        self.values = values
        self.operator = op
        self.result = 0

    def solve_problem(self):
        if self.operator == "*":
            self.result = self.values[0]
            for i in range(1, len(self.values)):
                self.result = self.result * self.values[i]
        elif self.operator == "+":
            for value in self.values:
                self.result += value

class Block:
    def __init__(self, start: int, stop: int):
        self.start_index = start
        self.stop_index = stop
