# Entrada do valor inicial e da quantidade de dias
valor = float(input())
dias_atraso = int(input())

# Calculo dos valores solicitados pelo exercicio
multa = valor * 0.02
juros = 0.00033 * dias_atraso * valor
valor_total = valor + multa + juros
valor_minimo = 0.1 * valor_total

print("Valor: R$", format(valor, '.2f'))
print("Multa: R$", format(multa, '.2f'))
print("Juros: R$", format(juros, '.2f'))
print("Valor total: R$", format(valor_total, '.2f'))
print("Valor minimo para renegociacao: R$", format(valor_minimo, '.2f'))
