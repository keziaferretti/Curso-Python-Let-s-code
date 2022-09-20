#Aula 12 Dicionario


# Criando Dicionarios 

dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Kézia', 'idade':28, 'altura': 1.58 }

print(dicionario)
print(dicionario ['idade'])



#Adicionar elementos em um dicionario

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 1.89
print(dicionario)

# Iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave] )

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)