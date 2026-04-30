num = float(input("Digite um número: "))

if num >= 0:
    print(f"{num} é positivo")
else:
    print(f"{num} é negativo")
# // <--- 1) Positivo ou negativo/


num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")
# // <--- 2) Par ou ímpar


n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

if n1 > n2:
    print(f"{n1} é maior")
elif n2 > n1:
    print(f"{n2} é maior")
else:
    print("São iguais")
# // <--- 3) Maior entre dois números


n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

maior = max(n1, n2, n3)
print(f"O maior número é {maior}")
# // <--- 4) Maior entre três números


c = float(input("Celsius: "))
f = (c * 9/5) + 32

print(f"{c}°C = {f}°F")
# // <--- 5) Celsius para Fahrenheit


idade = int(input("Digite a idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
else:
    print("Adulto")
# // <--- 6) Classificação por idade


n = int(input("Digite um número: "))

for i in range(1, n + 1):
    print(i)
# // <--- 7) Contagem até n


n = int(input("Digite um número: "))

for i in range(1, n + 1):
    print(i, end=" ")
# // <--- 8) Contagem até n (na mesma linha)