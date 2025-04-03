# exer 1
'''numero = int(input("Insira um número:"))
if numero % 2 == 0:
print("esse numero é par")
else:
print("esse número é impar")
'''

# exer 2
'''
numero = int(input("Insira um numero"))
if numero >= 10:
print("esse numero é maior que 10")
else:
print("esse numero é menor que 10")
'''

# exer 3
'''
idade = int(input("insira sua idade"))
if idade >= 18:
print("voce é maior de idade")
else:
print("voce é menor de idade")
'''
# exer 4
'''
idade = int(input("insira sua idade"))
if idade >= 18:
print("Seu voto é obrigatório")
elif idade >= 16:
print("Seu voto é opcional")
else:
print("voce não tem voto")
'''
# exer 5
'''
numero = int(input("insira um numero"))
if numero == 0:
print("o numero inserido é 0 ")
elif numero <= -1:
print("o numero inserido é negativo")
else:
print("o numero inserido é positivo")
'''
# exer 6
'''
nota = int(input("insira uma nota de 0 a 10"))
if nota == 10:
print("sua nota é A")
elif nota >= 9:
print("sua nota é A")
elif nota >= 7:
print("sua nota é B")
elif nota >= 5:
print("sua nota é C")
elif nota >= 3:
print("sua nota é D")
else:
print("sua nota é E")
'''

# exer 7
'''
idade =int(input("insira sua idade"))
if idade <= 12:
print("Você tem direito a um desconto! (Crianças até 12 anos)")
elif 13 <= idade <= 59:
print("Você não tem direito a desconto. (Adultos entre 13 e 59 anos)")
else:
print("Você tem direito a um desconto! (Idosos a partir de 60 anos)")

#exercicio 8
a = float(input("Digite o primeiro lado: "))

b = float(input("Digite o segundo lado: "))

c = float(input("Digite o terceiro lado: "))

*# Verifica se os lados formam um triângulo (desigualdade triangular)*

if (a + b > c) and (a + c > b) and (b + c > a):

*# Classifica o tipo de triângulo*

if a == b == c:

print("É um triângulo equilátero.")

elif a == b or a == c or b == c:

print("É um triângulo isósceles.")

else:

print("É um triângulo escaleno.")

else:

print("Os valores informados não formam um triângulo.")
'''

# exer 8


# exer 9
'''
valor_compra = float(input("Digite o valor total da compra: R$ "))

## Verifica em qual faixa de desconto a compra se encaixa

if valor_compra < 100:
desconto = 0.05  # 5% de desconto
elif 100 <= valor_compra <= 500:
desconto = 0.10  # 10% de desconto
else:
desconto = 0.15  # 15% de desconto

## Calcula o valor do desconto e o valor final com desconto aplicado

valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

## Exibe os resultados

print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")
'''

# exer 10
'''
ano = int(input("insira o ano"))
if ano % 4 == 0 :
print("esse ano é bissexto")
else:
print("esse ano não é bissexto")
'''

# exer 11
'''
altura = float(input("insira a sua altura"))
peso = float(input("insira o seu peso"))
imc = peso / (altura * altura)
if imc <= 18.5:
print("baixo peso")
elif imc >= 18.5 and imc <= 24.9:
print("normal")
elif imc >= 25 and imc <= 29.9:
print("sobrepeso")
elif imc >= 30 and imc <= 34.9:
print("obesidade")
elif imc >= 35 and imc <= 39.9:
print("obesidade mórbida")
else:
print("obesidade extrema")
'''

# exer 12
'''
'''
# exer 13
# exer 14
# exer 15
# exer 16
# exer 17
# exer 18
# exer 19


