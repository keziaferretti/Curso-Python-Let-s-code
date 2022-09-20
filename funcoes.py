# Aula 11 Funções 

#https://cursos.letscode.com.br/curso-digital/ad77ffa3-6dde-4efb-9e0d-3b14e60b097b/modulo/b1bf4c3f-41a2-46f0-bfe9-d3d22dce487c/topico/31de2884-6cd3-46f9-bf7e-6eaa491b57b1

#Criação de Funções

# Função Inicial

def saudacao():
    print('Seja bem Vindo!')
    print('Olá, foi um prazer ter você fazendo parte dessse curso!')

saudacao()
saudacao()

# Função com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem Vindo!, {nome}')
    print(f'Olá, foi um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Kézia', 'Python')
     
# Função com parâmetros default

def saudacao(nome, curso='Python'):
    print(f'Seja bem Vindo!, {nome}')
    print(f'Olá, foi um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Kézia')


# Funções com retorno

def soma(num1, num2):
    #print('Soma =', num1 + num2) não usa o print dentro da função, return melhor 
    return num1 + num2 #após o return não funciona nenhuma função

resultado = soma(5, 7)

print('O resultado da soma é ', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10, 20)

print(resultado)