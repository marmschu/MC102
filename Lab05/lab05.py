# Ao longo do código, distribuirei os impedimentos logo após a entrada. Caso ocorra impedimento,
# soma 1 n variavel 'impedimento' e caso seja igual a 0 até o final de todas as entradas, a pessoa estará apta a doar
impedimento = 0
motives = []

# Entrada da massa corporal e idade
body_mass = float(input())
age = int(input())
print("Massa corporal:", body_mass)
print("Idade:", age)

# Se massa corporal for menor que 50kg, possui impedimento
if body_mass < 50:
    motives.append("abaixo da massa corporal minima")
    impedimento += 1

# Se a pessoa tem 16 ou 17 anos, verifica a existencia da permissão dos responsáveis
if 15 < age < 18:
    auth_corp = str(input())
    print("Documento de autorizacao:", auth_corp)
    if auth_corp == 'N':
        motives.append("menor de 18 anos sem consentimento dos responsaveis")
        impedimento += 1

if age < 16:
    motives.append("menor de 16 anos")
    impedimento += 1
elif age > 69:
    motives.append("maior de 69 anos")
    impedimento += 1

# Entrada da verificação se possui sintomas, se viajou nos últimos 30 dias, se teve contato com caso suspeito ou
# confirmado de COVID-19, e se é a primeira doação
symp = str(input())
trav = str(input())
contact = str(input())
first_don = str(input())
print("Febre ou sintomas gripais:", symp)
print("Viagem recente ao exterior:", trav)
print("Contato com caso de COVID-19:", contact)
print("Primeira doacao:", first_don)

if age > 60 and first_don == 'S':
    motives.append("maior de 60 anos e primeira doacao")
    impedimento += 1
if symp == 'S':
    motives.append("febre ou sintomas gripais")
    impedimento += 1
if trav == 'S':
    motives.append("viagem recente ao exterior")
    impedimento += 1
if contact == 'S':
    motives.append("contato com caso de COVID-19")
    impedimento += 1

# Caso não seja a primeira doação, solicita a quantidade de doações que a pessoa fez nso últimos 12 meses
# Se a quantidade solicitada for maior que 0, solicita o tempo, em meses, desde a última doação
if first_don == 'N':
    cont_don = int(input())
    print("Doacoes nos ultimos 12 meses:", cont_don)

    if cont_don > 0:
        last_don = int(input())
        print("Meses desde ultima doacao:", last_don)

# Entrada do sexo da pessoa que irá doar
sex = str(input())
print("Sexo biologico:", sex)

if first_don == 'N':
    if sex == 'M':
        # noinspection PyUnboundLocalVariable,PyUnboundLocalVariable
        if 4 <= cont_don:
            motives.append('numero maximo de doacoes anuais foi atingido')
            impedimento += 1
        elif 2 >= last_don:
            motives.append('numero maximo de doacoes anuais foi atingido')
            impedimento += 1
    else:
        # noinspection PyUnboundLocalVariable,PyUnboundLocalVariable
        if 3 <= cont_don:
            motives.append('numero maximo de doacoes anuais foi atingido')
            impedimento += 1
        elif 3 >= last_don:
            motives.append('intervalo minimo entre as doacoes nao foi respeitado')
            impedimento += 1

# Se mulher, verifica possibilidade de gravidez
if sex == 'F':
    preg = str(input())
    print("Gravida ou amamentando:", preg)
    if preg == 'S':
        motives.append('gravida ou amamentando')
        impedimento += 1

for x in motives:
    print("Impedimento: " + x)

# Se impedimento == 0, a pessoa esta apta a doar
if impedimento == 0:
    print('Agende um horario para triagem completa')
