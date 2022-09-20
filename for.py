#Aula 8: Laços de Repetição ("For")
#criar repetição contralada, sabe quantas vezes vc vai repetir o codigo
# for -> para, in -> dentro, range ->faixa

#para essa variavel dentro de uma determinada faixa

#um parametro
# for variavel in range(5):
#     print(variavel)
    
# dois parametros
# for variavel in range(1, 10):
#     print(variavel)

#tres parametro
# for variavel in range(1, 12, 3):
#     print(variavel)

#Aplicação pratica

soma = 0


for i in range(1, 4):
    nota =float(input(f'Informe sua nota: {i} '))

    soma = soma + nota
    
print(soma / 3)
