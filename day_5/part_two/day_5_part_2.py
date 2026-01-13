with open("../input.txt", "r") as f:
    raw_content_lines = f.readlines()

# raw_content_lines = ["3-5", "10-14", "16-20", "12-13", "10-14"]
# raw_content_lines = ["10-14", "16-20", "10-13", "10-15"]

filtered_raw_content_lines = list(dict.fromkeys(raw_content_lines))
# print(filtered_raw_content_lines)

class IdRange:
    def __init__(self, str_range: str):
        self.range_min = int(str_range.split("-")[0])
        self.range_max = int(str_range.split("-")[1])

    def __repr__(self):
        return f"({self.range_min}-{self.range_max})"

raw_id_ranges_list: list[IdRange] = []

for raw_line in filtered_raw_content_lines:
    line = raw_line.strip()
    if "-" in line.strip():
        raw_id_ranges_list.append(IdRange(line))


sorted_id_ranges_tuple_list = sorted(raw_id_ranges_list, key=lambda this_id_range: (this_id_range.range_min, this_id_range.range_max))

class NewRange:
    def __init__(self, min_range: int, max_range: int):
        self.min_range = min_range
        self.max_range = max_range
        self.counter = len(range(self.min_range, self.max_range + 1))

    def set_min_range(self, new_min: int):
        self.min_range = new_min
        self.counter = len(range(self.min_range, self.max_range + 1))


    def set_max_range(self, new_max: int):
        self.max_range = new_max
        self.counter = len(range(self.min_range, self.max_range + 1))


# TODO: j'ai clean la source (pas doublons et sorted), il faut mainenant vérifier le slice sorted_id_ranges_tuple_list en comparant i et i + 1
# TODO: si i et i + 1 s'entrecroisent, on les supprimes de la liste et les remplace par une nouvelle range et on recommence
# TODO: a la fin on aura que des ranges indépendantes et on a plus qu'à compter

# TODO : class NewRange avec un set_data() pour gérer l'ajustement des bornes et stocker le compteur auto

new_ranges_list: list[NewRange] = []

for i in range(len(sorted_id_ranges_tuple_list)):
    current_id_range = sorted_id_ranges_tuple_list[i]
    if not new_ranges_list:
        first_new_range = NewRange(current_id_range.range_min, current_id_range.range_max)
        new_ranges_list.append(first_new_range)
        continue

    is_matching = False
    for j in range(len(new_ranges_list)):
        existing_new_range = new_ranges_list[j]
        if existing_new_range.min_range <= current_id_range.range_min <= existing_new_range.max_range or existing_new_range.min_range <= current_id_range.range_max <= existing_new_range.max_range:
            ranges_limits_list = [existing_new_range.min_range, current_id_range.range_min, existing_new_range.max_range, current_id_range.range_max]
            existing_new_range.set_min_range(min(ranges_limits_list))
            existing_new_range.set_max_range(max(ranges_limits_list))
            is_matching = True
            break
    if not is_matching:
        unmatched_new_range = NewRange(current_id_range.range_min, current_id_range.range_max)
        new_ranges_list.append(unmatched_new_range)

result = 0
for new_range in new_ranges_list:
    result += new_range.counter

print("Ranges count : ", len(new_ranges_list))
print("Result : ", result)