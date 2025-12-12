# On découvre que finalement le bon mot de passe est le nombre de fois que la molette passe par 0 (ou s'arrête sur 0)
# Et ceux pendant ou à la fin d'une rotation
# Avertissement : si la molette part de 50, R1000 la fait passer 10x par 0 avant de revenir à 50
from day_1.counter import Counter

# 1. Itérer sur le fichier txt pour en extraire une liste de int relatifs
# 2. Itérer sur les rotations de la liste pour faire :
# 2.1 On part de 50 (position de départ) donc position
# 2.2 On fait la rotation (donc plus ou moins une valeur) et on stock result
# 2.3 on vérifie si result < 0, si oui position = 100 - result et on incrémente password_counter
# 2.4 on vérifie si result > 100, si oui postion = 0 + result - 100 et on incrémente password_counter
# 3. on retourne password_counter

# 1. Itérer sur le fichier txt pour en extraire une liste de int relatifs

int_rotations_values_from_file = []

with open("input.txt", "r") as f:
    raw_content = f.readlines()

cleaned_content = []

for rotation in raw_content:
    cleaned_rotation = rotation.strip()
    # print(cleaned_rotation)
    cleaned_content.append(cleaned_rotation)

def convert_string_rotation_to_relative_int_value(str_rotation_value: str) -> int:
    if str_rotation_value.startswith("L"):
        int_rotation_value = - int(str_value.split("L")[1])
    else:
        int_rotation_value = int(str_value.split("R")[1])
    return int_rotation_value

int_rotations = []

for str_value in cleaned_content:
    int_value = convert_string_rotation_to_relative_int_value(str_value)
    # print(type(int_value))
    # print(int_value)
    int_rotations.append(int_value)

# print(type(int_rotations))
# print(int_rotations)

# 2. Itérer sur les rotations de la liste pour faire :
# 2.1 On part de 50 (position de départ) donc position
# position = 50
# password_counter = 0
# 2.2 On fait la rotation (donc plus ou moins une valeur) et on stock result
# 2.3 on vérifie si result < 0, si oui position = 100 - result et on incrémente password_counter
# 2.4 on vérifie si result > 99, si oui postion = result - 100 et on incrémente password_counter
counter = Counter(int_rotations)
# for rotation in int_rotations:
#     result = position + rotation
#     print("après rotation: ", result)
#
#     if position == 0 and rotation < 0:
#         password_counter -= 1
#         if result == 0:
#             password_counter += 1
#         else:
#             while result < 0:
#                 result = 100 + result
#                 password_counter += 1
#                 print("ajoute 100 incrémente 1: ", result)
#     else:
#         if result == 0:
#             password_counter += 1
#         else:
#             while result < 0:
#                 result = 100 + result
#                 password_counter += 1
#                 print("ajoute 100 incrémente 1: ", result)
#
#             while result > 99:
#                 result = result - 100
#                 password_counter += 1
#                 print("retire 100 incrémente 1: ", result)
#
#     position = result
# # 3. on retourne password_counter
# print(password_counter)

# Pour chaque rotation
# Si position = 0 et que rotation < 0, alors on ne doit pas compter le premier départ puis appliquer un while ensuite
