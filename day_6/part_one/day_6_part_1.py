with open("../input.txt", "r") as f:
    raw_content_lines = f.readlines()

print(raw_content_lines)

cleaned_content_lines = []
for raw_line in raw_content_lines:
    cleaned_content_lines.append(raw_line.strip())

print(cleaned_content_lines)

int_lines = []
for cleaned_line in cleaned_content_lines:
    no_duplicated_space_line = " ".join(cleaned_line.split())
    int_lines.append(no_duplicated_space_line.split())

print(int_lines)

class Problem:
    def __init__(self):
        self.values = []
        self.operator = ""
        self.result = 0

    def solve_problem(self):
        if self.operator == "*":
            self.result = self.values[0]
            for i in range(1, len(self.values)):
                self.result = self.result * self.values[i]
        elif self.operator == "+":
            for value in self.values:
                self.result += value

solved_problems_list = []
for i in range(len(int_lines[0])):
    new_problem = Problem()
    for j in range(len(int_lines)):
        if j == len(int_lines) - 1:
            new_problem.operator = int_lines[j][i]
        else:
            new_problem.values.append(int(int_lines[j][i]))
    new_problem.solve_problem()
    solved_problems_list.append(new_problem.result)

grand_total = sum(solved_problems_list)
print(grand_total)