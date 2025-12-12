from day_1.counter import Counter

int_rotations = [-63, 23, -10, -30, 250, -220]


# 2. Itérer sur les rotations de la liste pour faire :
# 2.1 On part de 50 (position de départ) donc position
position = 50
password_counter = 0
# 2.2 On fait la rotation (donc plus ou moins une valeur) et on stock result
# 2.3 on vérifie si result < 0, si oui position = 100 - result et on incrémente password_counter
# 2.4 on vérifie si result > 99, si oui postion = result - 100 et on incrémente password_counter

counter = Counter(int_rotations)
# Pour chaque rotation
# Si position = 0 et que rotation < 0, alors on ne doit pas compter le premier départ puis appliquer un while ensuite
