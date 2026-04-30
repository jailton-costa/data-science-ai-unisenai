
nomes = [
    "João", "Pedro", "Lucas", "Mateus", "Gabriel",
    "Maria", "Ana", "Juliana", "Fernanda", "Patrícia",
    "Rafael", "Bruno", "Carlos", "Felipe", "Marcos",
    "Mariana", "Amanda", "Letícia", "Renata", "Carla",
    "André", "Rodrigo", "Diego", "Fernando", "Ricardo",
    "Camila", "Aline", "Larissa", "Beatriz", "Carolina",
]

salarios = [
    15432, 1981, 1654, 11234, 1876,
    8450, 13210, 4654, 3321, 1999,
    2002, 11765, 19201, 3450, 1789,
    12100, 10456, 990, 970, 24032,
    5888, 2345, 7777, 5001, 20000,
    18800, 12666, 14700, 1101, 5000
]

# Imagine que os dados acima foram extraídos de uma planilha do RH

# Há quantos funcionários nessa empresa? 1

# Qual é o salário médio? 2

# Quantas pessoas ganham no mínimo 20% acima da média? 3

# Quantas pessoas ganham no mínimo 20% abaixo da média?

# Quem é a pessoa que tem o maior salário?

# Quem é a pessoa que tem o menor salário?

# Qual é o tamanho da folha de pagamentos? (considerem 13 meses de salário e 1/3 de férias, desconsiderem impostos)

# Qual é o salário anual de cada funcionário, incluíndo 13o e 1/3 de férias?

VERDE = "\033[32m"
AMARELO = "\033[33m"
VERMELHO = "\033[31m"
RESET = "\033[0m"

print(f"{AMARELO}\n----( Seja Bem Vindo Ao Sistema Do RH )----{RESET}\n")
print(f"{VERDE}Análise de dados dos funcionários - (1){RESET}\n{VERDE}Qual é o salário médio - (2){RESET}")
print(f"{VERDE}Quantas pessoas ganham no mínimo 20% acima da média - (3){RESET}")
print(f"{VERDE}Quantas pessoas ganham no mínimo 20% abaixo da média - (4){RESET}")
print(f"{VERDE}Quem tem o maior salário - (5){RESET}\n{VERDE}Quem tem o menor salário - (6){RESET}")
print(f"{VERDE}Qual é o tamanho da folha de pagamentos? - (7){RESET}")
print(f"{VERDE}Salário anual com 13º + férias - (8){RESET}")

while True:
    objetivo = input("\nDigite o número da opção que deseja analisar ou 'p' para encerrar: ").strip().lower()
    match objetivo:
        case "p":
            print(f"{AMARELO}ok, encerrando...{RESET}")
            break
        case "1":
            print(f"{VERDE}Há {len(nomes)} funcionários nessa empresa{RESET}")
        case "2":
            print(f"{VERDE}O salário médio é {sum(salarios) / len(salarios):.2f}{RESET}")
        case "3":
            media = sum(salarios) / len(salarios)
            cont  = sum(1 for salario in salarios if salario >= media * 1.2)
            print(f"{VERDE}Há {cont} pessoas que ganham no mínimo 20% acima da média{RESET}")
        case "4":
            media = sum(salarios) / len(salarios)
            cont  = sum(1 for salario in salarios if salario <= media * 0.8)
            print(f"{VERDE}Há {cont} pessoas que ganham no mínimo 20% abaixo da média{RESET}")
        case "5":
            max_salario = max(salarios)
            indice = salarios.index(max_salario)
            print(f"{VERDE}A pessoa com o maior salário é {nomes[indice]} com R$ {max_salario:.2f}{RESET}")
        case "6":
            min_salario = min(salarios)
            indice = salarios.index(min_salario)
            print(f"{VERDE}A pessoa com o menor salário é {nomes[indice]} com R$ {min_salario:.2f}{RESET}")
        case "7":
            total = sum(salarios) * 13 + sum(salarios) / 3
            print(f"{VERDE}O tamanho da folha de pagamentos é R$ {total:.2f}{RESET}")
        case "8":
            for i, salario in enumerate(salarios):
                anual = salario * 13 + salario / 3
                print(f"{VERDE}{nomes[i]}: R$ {anual:.2f}{RESET}")
        case _:
            print(f"{VERMELHO}desculpe, não entendi. tente novamente{RESET}")

