from day_2.id_ranges import IdRange
from day_2.id_strings import IdString

with open("input.txt", "r") as f:
    content = f.read()

id_ranges_list = []

for raw_id_range in content.split(","):
    id_ranges_list.append(IdRange(raw_id_range))

# print(id_ranges_list)

invalid_ids_list = []

for id_range in id_ranges_list:
    for id_to_check in range(id_range.id_min, int(id_range.id_max) + 1):
        # on décompose l'id en slice de 1 et on vérifie si elles sont toutes égales
        # puis en slice de deux (si int(result) -> True)
        # puis en slice de trois, etc... jusqu'à len()
        # dès qu'une vérif est vraie, on ajoute aux id invalides
        id_string = IdString(id_to_check)
        for available_slicing_value in id_string.available_slicing_values:
            slices = id_string.slice_id(available_slicing_value)
            id_string.errors = 0
            for i in range(0, len(slices) - 1):
                if slices[i] != slices[i + 1]:
                    id_string.errors += 1

            if not id_string.errors:
                invalid_ids_list.append(id_to_check)
                break

result = sum(invalid_ids_list)
print(invalid_ids_list)
print(result)
