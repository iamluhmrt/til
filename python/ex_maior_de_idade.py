ano_base = 2023
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))
ano_nascimento = ano_base - idade
aniversario = input('Você fez aniversário esse ano?: ')
altura_metros = float(input('Digite sua altura: '))
if aniversario == "no" or "não":
  ano_nascimento -= 1
maior_de_idade = idade >= 18
print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de nascimento: ', ano_nascimento)
print('É maior de idade? ', maior_de_idade)
print('Altura em metros: ', altura_metros)
