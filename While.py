# Aula 7: Laços de Repetição ("While") condicional 

# While -> enquanto

numero_sorteado = 15

numero_escolhido = int(input('Informe um numero entre 1 e 20: '))

while numero_escolhido != numero_sorteado: 
    print('Você errou número, tente novamente....')

    numero_escolhido = int(input('Informe um numero entre 1 e 20: '))

print('Parabéns você acertou!')

#Exemplo 2: Estrutura com contador

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1