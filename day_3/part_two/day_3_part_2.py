from day_3.part_two.battery_bank import BatteryBank

with open("../input.txt", "r") as f:
    content_lines = f.readlines()

# 1. Pour chaque ligne, on slice à [:-11] pour être sûr d'avoir 12 digit dispos
# 2. sur la première portion, on cherche le max mais en les comparant un à un (n et n + 1), dès que n > n + 1 on arrête et garde n (value et index)
# 3. on slice maintenant la ligne sur l'index du max (pour prendre tout ce qu'il y a après) et on tri ordre croissant les values)
# 4. on garde les 11 dernières valeurs du sort (11 plus grosses)
# 5. on concatène pour faire notre value power à 12 digit et on stocke dans une liste
# 6. on calcul sum(liste)

results_list: list[int] = []

for line in content_lines:
    battery_bank = BatteryBank(line)
    results_list.append(int(battery_bank.result))
    print(int(battery_bank.result))

print(sum(results_list))