#Aula 6 let's code Americanas 

#Maior de idade

from turtle import pensize


idade = int(input('Qual é a sua idade: '))

if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')

#media do aluno

media = float(input('Informe a média do estudante: '))

if media >= 7:
    print('Você passou de ano')
else:
    print('Você reprovou de ano')


#Else if --> Elif
media = float(input('Informe a média do estudante: '))

if media >= 7:
    print('Você passou de ano')
elif media >=5:
    print('Recuperação')
else:
    print('Você reprovou de ano')


#

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovado')
else:
    print('Reprovado')