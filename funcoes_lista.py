#Aula 10 Métodos e Funções de Listas 

# . Método de listas 

lista = [1, 3, 12, 8, 2]

#append -> acionar um elemento no final da lista

print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)

# insert -> escolhe a posição e qual elemento quer adionar 

lista.insert(2, 10)
print('Depois do insert: ', lista)

#extend - juntar duas listas, pega elemento da lista 2 e colocar no final

lista2 = [1, 2, 3]

lista.extend(lista2)
print('Depois do extend: ', lista)

#pop - remover o ultimo elemento,  ou que vc especificar

lista.pop()
print('Depois após do pop: ', lista)

lista.pop(0)
print('Depois após do pop: ', lista)


# remove - vc diz qual valor que vc quer tirar (remove o primeiro que encontra)

lista.remove(3)

print('Depois após do remove: ', lista)


#count - contar quantas vezes o elemento aparece na lista

print('Qauntudade de 2 na lista: ', lista.count(2))

#index - o indice do determinado elemento na lista

print('Indice do elemento 12: ', lista.index(12))

#sort - ordenar alista

lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)


#FUNÇÕES PARA LISTAS

# Len

print(len(lista))

# sum - soma

print(sum(lista))


# max

print('Maior elemento da lista: ' , max(lista))

# min
print('Menor elemento da lista: ' , min(lista))