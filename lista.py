#Aula 9: Estrutura de Listas
#estrura que guarda todas variaveis

#Comn listas
notas = [10, 7, 9]

#Criando Listas
lista = []
lista = list()
lista = [26, 'Walisson', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

#Indexação e Slices (Fatiamento)
lista = [10, 'kezia', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])


# Slices  -  fatiamento

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])


# > Iterações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizano os índices - tamanho da lista

print('Comprimento da lista ', len(lista))

for i in range(len(lista)):  #mesma coisa que colocar 7
    print(lista[i])
