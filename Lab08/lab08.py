# MARINA_MILENY
# 221979
# Turma_6

lista = input().split()

lista_num = " "
lista_palavras = " "
lista_hashtag = " "
lista_emoticon = " "

for i in lista:
    if i.isdigit() or (i[1:].isdigit() and i.find("-") == 0):
        lista_num = lista_num + i + " "

    elif i.isalpha():
        lista_palavras = lista_palavras + i + " "

    elif i.find("#") == 0 and i[1:].isalpha():
        lista_hashtag = lista_hashtag + i + " "
    else:
        lista_emoticon = lista_emoticon + i + " "

print("Palavra(s):", lista_palavras[:-1], sep = "")
print("Numero(s):", lista_num[:-1], sep = "")
print("Hashtag(s):", lista_hashtag[:-1], sep = "")
print("Emoticon(s):", lista_emoticon[:-1], sep = "")
