# Exercício IMC - Curso de Python. 
nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)
print(f'{nome} tem {altura:.2f} de altura e pesa {peso} e o seu IMC é \n{imc:.2f}')