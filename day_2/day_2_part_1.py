# 1. Il faut séparer sur les virgules d'abord (ranges), puis sur les "-" (borne min et max)
# 2. Récupérer une liste d'objets IdRange (2 bornes)
# 3.1 Pour chaque IdRange, il faut parcourir chaque ID (incrémentation)
# 3.2 On prend la longueur de la chaine (ex: 6 caractères)
# 3.3 On coupe en deux (split après le 3ème caractère)
# 3.4 Id invalid si les deux chaînes sont égales
# 4. on ajoute dans une liste les ID invalides
# 5. invalid_ids_list.sum()
from day_2.id_ranges import IdRange

with open("input.txt", "r") as f:
    content = f.read()

id_ranges_list = []

for raw_id_range in content.split(","):
    id_ranges_list.append(IdRange(raw_id_range))

# print(id_ranges_list)

invalid_ids_list = []

for id_range in id_ranges_list:
    for id_to_check in range(id_range.id_min, int(id_range.id_max) + 1):
        if len(str(id_to_check)) % 2 == 0:
            id_size_by_two = int(len(str(id_to_check)) / 2)
            first_slice = str(id_to_check)[:id_size_by_two]
            second_slice = str(id_to_check)[id_size_by_two:]

            if first_slice == second_slice:
                invalid_ids_list.append(id_to_check)

result = sum(invalid_ids_list)
print(invalid_ids_list)
print(result)