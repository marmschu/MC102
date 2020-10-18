# MARINA_MILENY
# 221979
# Turma_6

t = float(input())
nivel_0 = []
nivel_1 = []
nivel_2 = []
all_lvl = []

while t != -1:
    if t < 180:
        nivel_0.append(t)
        all_lvl.append(t)
    elif t < 240:
        nivel_1.append(t)
        all_lvl.append(t)
    else:
        nivel_2.append(t)
        all_lvl.append(t)
    t = float(input())

media = round((sum(all_lvl) / len(all_lvl)), 1)
vel_max = round((33 / (min(all_lvl) / 60)), 1)
vel_min = round((33 / (max(all_lvl) / 60)), 1)

print("Caracois no nivel 0:", len(nivel_0))
print("Caracois no nivel 1:", len(nivel_1))
print("Caracois no nivel 2:", len(nivel_2))
print("Tempo medio:", media, "s")
print("Velocidade maxima:", vel_max, "cm/min")
print("Velocidade minima:", vel_min, "cm/min")
