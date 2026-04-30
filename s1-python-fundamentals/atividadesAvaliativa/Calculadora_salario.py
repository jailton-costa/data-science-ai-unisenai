# Crie um programa capaz de calcular o salário líquido do trabalhador.
# Requisitos:
#
# 1. Crie uma função capaz de calcular o desconto do INSS.
#
# Faixa salarial (R$)	Alíquota
# Até 1.412,00	7,5%
# De 1.412,01 até 2.666,68	9%
# De 2.666,69 até 4.000,03	12%
# De 4.000,04 até 7.786,02	14%
#
# Você não aplica uma única alíquota sobre todo o salário.
#
# Divida o salário em faixas:
# Exemplo (salário de R$ 3.000):
# 1.412,00 × 7,5%
# (2.666,68 − 1.412,00) × 9%
# (3.000 − 2.666,68) × 12%
#
# e some tudo.
# OBS: Existe um limite máximo: 7786,02. Acima desse valor não há mais desconto.
#
# 2. Crie uma função capaz de calcular o Imposto de Renda:


def calcular_desconto_inss(salario: float) -> float:
    TETO_INSS = 7786.02
    base = min(salario, TETO_INSS)

    desconto = 0.0
    if base > 4000.03:
        desconto += (base - 4000.03) * 0.14
        base = 4000.03
    if base > 2666.68:
        desconto += (base - 2666.68) * 0.12
        base = 2666.68
    if base > 1412.00:
        desconto += (base - 1412.00) * 0.09
        base = 1412.00
    desconto += base * 0.075
    return desconto

def calcular_desconto_irpf(salario: float) -> float:
    return salario * 0.27

salario_bruto = 0.0

while salario_bruto < 7786.02:
    salario_bruto = float(input("\nDigite seu salário bruto total: "))
    if salario_bruto <= 0:
        print("Salário inválido. O valor deve ser positivo.\n")
        continue
    elif salario_bruto > 7786.02:
        print("Salário acima do limite máximo. Não é possível calcular o desconto. tente novamente.\n")
        continue    
    else:
        print("\nCalculando salário líquido...")
        break

desconto_inss = calcular_desconto_inss(salario_bruto)
base_irpf = salario_bruto - desconto_inss
desconto_irpf = calcular_desconto_irpf(base_irpf)
salario_liquido = salario_bruto - desconto_inss - desconto_irpf

print(f"\nSalário bruto: R$ {salario_bruto:.2f}")
print(f"INSS: R$ {desconto_inss:.2f}")
print(f"IRPF: R$ {desconto_irpf:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}\n") 