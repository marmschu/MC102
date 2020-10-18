# Entrada dos lados de um triângulo, independente da ordem
A = float(input())
B = float(input())
C = float(input())

# Vamos estabeler um valor para a variável que nos auxiliará na resolução dos triângulos acutângulo, retângulo e
# obtusângulo. A variavel calcula a diferença entre o quadrado do lado em questão e a soma do quadrado do restante
# dos lados
var_lado_A = A * A - B * B - C * C
var_lado_B = B * B - A * A - C * C
var_lado_C = C * C - B * B - A * A

if A <= 0 or B <= 0 or C <= 0 or A >= B + C or B >= C + A or C >= B + A:
    print("Valores invalidos na entrada")
else:
    if A == B == C:
        print("Triangulo equilatero")
    elif A == B or B == C or A == C:
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")

    if A >= B and A >= C:
        if var_lado_A < 0:
            print("Triangulo acutangulo")
        elif var_lado_A == 0:
            print("Triangulo retangulo")
        else:
            print("Triangulo obtusangulo")
    elif B >= C:
        if var_lado_B < 0:
            print("Triangulo acutangulo")
        elif var_lado_B == 0:
            print("Triangulo retangulo")
        else:
            print("Triangulo obtusangulo")
    else:
        if var_lado_C < 0:
            print("Triangulo acutangulo")
        elif var_lado_C == 0:
            print("Triangulo retangulo")
        else:
            print("Triangulo obtusangulo")
