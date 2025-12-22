from day_3.batteries import Batterie

with open("input.txt", "r") as f:
    content_lines = f.readlines()

batteries_list = []

for line in content_lines:
    battery = Batterie(line)
    batteries_list.append(battery.max_value_number)

print("result : ", sum(batteries_list))
# 1. Pour chaque ligne, on slice [:-1] (pour avoir un digit en rab)
# 2. ensuite on cherche le max sur la première portion et on trouve son index
# 3. On reprend la ligne de base et on la slice à l'index du max + 1
# 4. On cherche la valeur max sur cette deuxième portion
# 5. On concatène puis int() les deux digits dans une résult list
# 6. On calcule sum() de cette liste