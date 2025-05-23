# exer 1
'''numero = int(input("Insira um número:"))
if numero % 2 == 0:
print("esse numero é par")
else:
print("esse número é impar")


# exer 2
numero = int(input("Insira um numero"))
if numero >= 10:
print("esse numero é maior que 10")
else:
print("esse numero é menor que 10")



# exer 3
idade = int(input("insira sua idade"))
if idade >= 18:
print("voce é maior de idade")
else:
print("voce é menor de idade")


# exer 4
idade = int(input("insira sua idade"))
if idade >= 18:
print("Seu voto é obrigatório")
elif idade >= 16:
print("Seu voto é opcional")
else:
print("voce não tem voto")



# exer 5
numero = int(input("insira um numero"))
if numero == 0:
print("o numero inserido é 0 ")
elif numero <= -1:
print("o numero inserido é negativo")
else:
print("o numero inserido é positivo")


# exer 6
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



# exer 7
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

# Verifica se os lados formam um triângulo (desigualdade triangular)*

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


# exer 9

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


# exer 10

ano = int(input("insira o ano"))
if ano % 4 == 0 :
print("esse ano é bissexto")
else:
print("esse ano não é bissexto")


# exer 11
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


# exer 12
num1 = int(input("insira o primeiro numero"))
num2 = int(input("insira o segundo numero"))
num3 = int(input("insira o terceiro numero"))
if num1 > num2 > num3:
print("esta em ordem decrescente")
elif num1 < num2 < num3:
print("esta em ordem crescente")
else:
print("os numero são iguais")


# exer 13
temperatura = float(input("insira a temperatura em celsius"))
if temperatura <=10:
print("a temperatura é fria")
elif temperatura >= 10 and temperatura <=20:
print("a temperatura inserida é aconchegante")
elif temperatura >=25 and temperatura <=40:
print("a temperatura inserida é quente")
else:
print("a temperatura inserida é muito quente")


# exer 14
from datetime import datetime

data1 = input("insira uma data no formato 'dd/mm/aaaa")
data2 = datetime.strptime(data1, "%d/%m/%Y")
print(data2)


# exer 15
import re

senha = input("Insira uma senha: ")
if len(senha) < 8:
print("Senha inválida")
print("A senha deve ter no minimo 8 caracteres.")
elif senha.islower():
print("Senha inválida")
print("A senha precisa ter pelo menos um caractere maiusculo.")
elif senha.isalpha():
print("Senha inválida")
print("A senha precisa ter um número.")
elif senha.isalnum():
print("Senha inválida")
print("A senha precisa de um caracter especial.")
else:
print("Senha válida")


# exer 16
num = float(input("digite um numero:"))

if num < 0:
print("Insira um numero maior que 0 ")
elif num > 100:
print("insira um numero menor que 100")
else:

calculo = num ** (1/2)
print(f"A raiz quadrada do numero inserido é {num} é {calculo:,.2f}")


# exer 17
import re

data = input("Digite uma data (dd/mm/aaaa): ")
padrao = r"^\d{2}/\d{2}/\d{4}$"
valido = re.match(padrao, data)

if valido:
    dia, mes, ano = data.split('/')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    data_invertida = f'{ano:04d}-{mes:02d}-{dia:02d}'

    if mes == 2:
        # Verifica ano bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if 1 <= dia <= 29:
                print(f'A data formatada é: {data_invertida}')
            else:
                print("Dia inválido para fevereiro em ano bissexto")
        else:
            if 1 <= dia <= 28:
                print(f'A data formatada é: {data_invertida}')
            else:
                print("Dia inválido para fevereiro")
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
            print(f'A data formatada é: {data_invertida}')
        else:
            print("Dia inválido para esse mês")
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30:
            print(f'A data formatada é: {data_invertida}')
        else:
            print("Dia inválido para esse mês")
    else:
        print("Mês inválido")
else:
    print("Formato incorreto. Use dd/mm/aaaa")


# exer 18
conta = str(input("insira uma conta com as operações (+), (-), (*) ou (/)"))
resultado = eval(conta)
print(resultado)


# exer 19
cpf = input("Digite o CPF (somente números): ")

# Verifica se o CPF tem exatamente 11 dígitos
if len(cpf) != 11 or not cpf.isdigit():
    print("CPF Inválido")
else:
    # Cálculo do primeiro dígito verificador
    soma1 = int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6 + int(cpf[5]) * 5 + int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2
    resto1 = soma1 % 11
    if resto1 < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto1

    # Cálculo do segundo dígito verificador
    soma2 = int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + digito1 * 2
    resto2 = soma2 % 11
    if resto2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto2

    # Verificação final
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        print("CPF Válido")
    else:
        print("CPF Inválido")
  '''



