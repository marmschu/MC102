# MARINA_MILENY
# 221979
# Turma_6

obje_type = str(input())
charac = str(input())
dim = int(input())

if obje_type == "Q" and dim >= 3:
    for i in range(dim):
        print(charac * dim)

if obje_type == "T" and dim >= 3:
    for i in range(1, dim + 1):
        print((dim - i) * " " + ((i * 2) - 1) * charac)

if obje_type == "L" and dim >= 3:
    for i in range(1, dim + 1):
        print((dim - i) * " " + ((i * 2) - 1) * charac)
    for i in range(dim, 1, -1):
        print(((dim + 1 - i) * " ") + ((i * 2) - 3) * charac)

if obje_type == "H" and dim >= 3:
    for i in range(dim, 2 * dim):
        print((((2 * dim - 1) - i) * " ") + (2 * i - dim) * charac)
    for i in range(2 * dim - 2, dim - 1, -1):
        print(((2 * dim - i - 1) * " ") + (i * 2 - dim) * charac)

if obje_type == "O" and dim >= 3:
    for i in range(dim, 2 * dim):
        print((((2 * dim - 1) - i) * " ") + (2 * i - dim) * charac)
    for i in range(dim - 1):
        print(charac * (3 * dim - 2))
    for i in range(2 * dim - 2, dim - 1, -1):
        print(((2 * dim - i - 1) * " ") + (i * 2 - dim) * charac)

if obje_type != "Q" and obje_type != "T" and obje_type != "L" and obje_type != "H" and obje_type != "O":
    print("Identificador invalido.")

elif dim < 3:
    print("Dimensao invalida.")
