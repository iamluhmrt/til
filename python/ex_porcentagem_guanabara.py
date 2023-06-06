# Faça um algoritmo que leia opreço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: '))
novo_preco = preco - (preco * 5 / 100)
print(f'O produto que custava {preco:.2f}, na promoção com desconto de 5% vai custar R${novo_preco:.2f}')