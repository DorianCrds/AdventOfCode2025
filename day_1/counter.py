class Counter:
    def __init__(self, int_rotations: list[int]):
        self.rotations_list = int_rotations
        self.position = 50
        self.password = 0

        self.solve_problem()

    def solve_problem(self):
        for rotation in self.rotations_list:
            if rotation < 0:
                for i in range(rotation, 0):
                    self.position -= 1
                    if self.position == 0:
                        self.increment_counter()
                    if self.position < 0:
                        self.position = 99

            if rotation > 0:
                for i in range(rotation):
                    self.position += 1
                    if self.position > 99:
                        self.position = 0
                        self.increment_counter()
        print(self.password)

    def increment_counter(self) -> None:
        self.password += 1
