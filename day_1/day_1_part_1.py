# les elfes ont découvert la gestion de projet
# Ils savent que les décorations du Pôle Nord doivent être terminées rapidement pour que les autres tâches critiques puissent commencer à temps
# Mauvaise nouvelle : ils ont une autre urgence. Aucun d'entre eux n'a de temps disponible sur son planing pour s'en occuper.
# Je dois aider à décorer le Pôle Nord d'ici le 12 Décembre.
# Tous les jours 2 puzzles, le deuxième est déverrouillé à la résolution du premier
# Chaque puzzle rapporte une étoile
# J'arrive à la porte du Pôle Nord, prêt à décorer. Malheureusement, le mot de passe semble avoir été changé.
# Le cadena possède une molette avec des chiffre de 0 à 99
# Dans le doc il y a une série de rotations, une par ligne. Elles commencent par L (nbs inférieurs) ou R (nbs supérieurs)
# Une valeur de distance indique le nombre de clics à tourner
# Si le cadran est à 0, L1 fait pointer sur 99 et si cadran à 99, R1 fait pointer à 0.
# Le cadran pointe à 50 au départ
# Le mot de passe est en fait le nb de fois ou le cadran reste sur 0 après une rotation.
from pprint import pprint

# 1. Itérer sur le fichier txt pour en extraire une liste de int relatifs
# 2. Trouver la somme des nombre négatifs (le mini absolu) et pareil pour les valeurs positives (max absolu)
# 3. Déterminer les bornes à la centaine près (ex: -856 -> -900 et 427 -> 500) pour la liste de ticks
# 4. Générer la liste de ticks de centaines [-500, -400, -300,..., 600, 700] par exemple
# 5. Itérer sur la liste d'entier (rotations) pour les ajouter ou soustraire à la valeur de départ (50)
# 6. Vérifier pour chaque rotation si le résulat vaut 0, si oui -> incrémenter un compteur
# 7. Retourner en fin de boucle le compteur.

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

# 5. Itérer sur la liste d'entier (rotations) pour les ajouter ou soustraire à la valeur de départ (50)
# 6. Vérifier pour chaque rotation si le résulat est une valeur de centaine (ou 0), si oui -> incrémenter un compteur
def is_value_hundred_tick(value: int) -> bool:
    result = value / 100
    if result.is_integer():
        return True
    else:
        return False

password_counter = 0
dial_position = 50
for rotation in int_rotations:
    print(f"dial position : {dial_position} + {str(rotation)}")
    dial_position += rotation
    print("new position: ", dial_position)
    if is_value_hundred_tick(dial_position):
        password_counter += 1

# 7. Retourner en fin de boucle le compteur.
print(password_counter)