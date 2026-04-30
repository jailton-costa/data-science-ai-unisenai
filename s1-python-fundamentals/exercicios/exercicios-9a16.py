n = int(input("Digite um número: "))

numeros = [str(i) for i in range(1, n + 1)]
print(", ".join(numeros))
# // <--- 9) Contagem até n (na mesma linha)

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
op = input("Operação (+ - * /): ")

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    if n2 != 0:
        print(n1 / n2)
    else:
        print("Divisão por zero")
else:
    print("Operação inválida")
# // <--- 10) Calculadora simples

numeros = []

while True:
    entrada = input("Digite um número (ENTER para sair): ")

    if entrada == "":
        break

    numeros.append(float(entrada))

if numeros:
    media = sum(numeros) / len(numeros)
    print(f"Média: {media}")
else:
    print("Nenhum número informado")
# // <--- 11) Média de números


numeros = []

while True:
    entrada = input("Digite um número (ENTER para sair): ")

    if entrada == "":
        break

    numeros.append(int(entrada))

pares = [n for n in numeros if n % 2 == 0]

print("Resultado:", ", ".join(map(str, pares)))
# // <--- 12) Números pares


numeros = []
vistos = set()

while True:
    entrada = input("Digite um número (ENTER para sair): ")

    if entrada == "":
        break

    num = int(entrada)

    if num in vistos:
        print(f"Primeira repetição: {num}")
        break

    vistos.add(num)
# // <--- 13) Primeira repetição


numeros = []
repetidos = set()

while True:
    entrada = input("Digite um número (ENTER para sair): ")

    if entrada == "":
        break

    num = int(entrada)

    if num in numeros:
        repetidos.add(num)

    numeros.append(num)

print("Repetidos:", ", ".join(map(str, repetidos)))
# // <--- 14) Números repetidos


while True:
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("s - Sair")

    op = input("Opção: ").lower()

    if op == "s":
        break

    if op == "1":
        print("Opção Somar escolhida")
    elif op == "2":
        print("Opção Subtrair escolhida")
    elif op == "3":
        print("Opção Multiplicar escolhida")
    elif op == "4":
        print("Opção Dividir escolhida")
    else:
        print("Opção inválida")
# // <--- 15) Menu interativo


user = 6 

while user != 0:
  print("\n--- Calculadora Simples ---")
  user = int(input("(somar-1) (subtrair-2) (multiplicar-3) (dividir-4) (sair-0): "))

  if user == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))  
    numFim = num1 + num2
    print(f"O resultado da soma é {num1} + {num2} = {numFim}")

  elif user == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    numFim = num1 - num2
    print(f"O resultado da subtração é {num1} - {num2} = {numFim}")

  elif user == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    numFim = num1 * num2
    print(f"O resultado da multiplicação é {num1} * {num2} = {numFim}")

  elif user == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 != 0:
      numFim = num1 / num2
      print(f"O resultado da divisão é {num1} / {num2} = {numFim}")
    else:
      print("Erro: Não é possível dividir por zero!")

  elif user == 0:
    print("Calculadora encerrada.")

  else:
    print("Parece que houve um erro de digitação. Por favor, escolha uma opção válida.")
# // <--- 16) Calculadora com menu e loop