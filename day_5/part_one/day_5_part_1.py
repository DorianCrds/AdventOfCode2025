with open("../input.txt", "r") as f:
    raw_content_lines = f.readlines()

# print(raw_content_lines)

class IdRange:
    def __init__(self, str_range: str):
        self.range_tuple = (int(str_range.split("-")[0]), int(str_range.split("-")[1]))
        self.range_valid_ids = range(self.range_tuple[0], self.range_tuple[1] + 1)

ranges_list = []
ingredients_ids = set()

print("Processing raw content lines")
for raw_line in raw_content_lines:
    line = raw_line.strip()
    if "-" in line.strip():
        ranges_list.append(IdRange(line).range_valid_ids)
    elif line != "":
        ingredients_ids.add(int(line.strip()))
print("Raw lines loaded to get our range list and ingredients list")

fresh_ingredients_count = 0

for ingredient in ingredients_ids:
    for id_range in ranges_list:
        if ingredient in id_range:
            fresh_ingredients_count += 1
            break

print("Fresh ingredients : ", fresh_ingredients_count)
