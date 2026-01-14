# Ce que je sais :
# 1. Dans le fichier d'input, les blocs sont identifiables grâce aux index de leur colonnes : (i -> (i + 1) - 2)
# où i est index opérateur et -2 car il y a une colonne vide de séparation
# 2. On doit lire de droite à gauche les problèmes
# en respectant l'index de colonne de chaque digit

# TODO: objet Bloc, qui a index de début, index de fin, col_count, row_count et une liste de str strippée (chaine représentant une colonne)
# TODO: l'objet Problem ne doit pas bouger théoriquement il fait la même chose

from day_6.part_two.items import Block, Problem

with open("../input.txt", "r") as f:
    raw_content_lines = f.readlines()

# print(raw_content_lines)

filled_content_lines = []
required_line_length = 0
for raw_line in raw_content_lines:
    if len(raw_line) > required_line_length:
        required_line_length = len(raw_line)
    # print(required_line_length)

for raw_line in raw_content_lines:
    if len(raw_line) < required_line_length:
        raw_line += (" " * (required_line_length - len(raw_line)))
    # print(len(raw_line))
    # print("Filled line length : ", len(raw_line))
    # print(list(raw_line))

# print("Raw content filled with spaces : ", raw_content_lines)

content_lines_as_lists = []

for raw_line in raw_content_lines:
    content_lines_as_lists.append(list(raw_line))
# print("Content as lists : ", content_lines_as_lists)

block_limits_indexes_list = []

lines_count = len(content_lines_as_lists)
last_line_index = lines_count - 1
# print("Last line index : ", last_line_index)
for i in range(len(content_lines_as_lists[last_line_index])):
    if content_lines_as_lists[last_line_index][i] == "+" or content_lines_as_lists[last_line_index][i] == "*":
        block_limits_indexes_list.append(i)
block_limits_indexes_list.append(required_line_length)
# print("Bloc limits list : ", block_limits_indexes_list)

blocks = []
for i in range(len(block_limits_indexes_list) - 1):
    new_block = Block(block_limits_indexes_list[i], block_limits_indexes_list[(i + 1)] - 2)
    # print(block_limits_indexes_list[i], block_limits_indexes_list[(i + 1)] - 2)
    blocks.append(new_block)

# print(blocks)

results = []

for block in blocks:
    int_values: list[int] = []
    for i in range(block.start_index, block.stop_index + 1):
        value_str = ""
        for j in range(last_line_index):
            if content_lines_as_lists[j][i].isdigit():
                value_str += content_lines_as_lists[j][i]
                print(content_lines_as_lists[j][i])
        print(value_str)
        int_values.append(int(value_str))

    print(int_values)
    problem_solved = Problem(int_values, content_lines_as_lists[last_line_index][block.start_index])
    problem_solved.solve_problem()
    results.append(problem_solved.result)

print("Result : ", sum(results))