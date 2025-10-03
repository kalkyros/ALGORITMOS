def calcula_bonificacao(taxa_bonus, salario_base):
    fator_bonus = taxa_bonus / 100
    valor_bonificacao = salario_base * fator_bonus  
    novo_salario = salario_base + valor_bonificacao   
    return novo_salario

def main():
    while True:
        try:
            salario_base_input = input("informe o salário base do funcionário: R$ ")
            salario_base = float(salario_base_input.replace(',', '.'))
            if salario_base < 0:
                 print("o salário base não pode ser negativo.tente novamente.")
            else:
                break
        except ValueError:
            print("entrada inválida. digite um valor numérico para o salário.")
    while True:
        try:            
            taxa_bonus_input = input("informe a taxa de bonificação de produção: ")
            taxa_bonus = float(taxa_bonus_input.replace(',', '.'))
            if taxa_bonus < 0:
                 print("a taxa de bonificação não pode ser negativa. tente novamente.")
            else:
                break
        except ValueError:
            print("entrada inválida. digite um valor numérico para a taxa.")   
    salario_final = calcula_bonificacao(taxa_bonus, salario_base) 
    fator_bonus = taxa_bonus / 100
    bonificacao_concedida = salario_base * fator_bonus
    print(f"Salário Base Informado:    R$ {salario_base:,.2f}".replace('.', '#').replace(',', '.').replace('#', ','))
    print(f"Taxa de Bonificação:       {taxa_bonus:,.2f}%".replace('.', '#').replace(',', '.').replace('#', ','))
    print(f"Bonificação Concedida:     R$ {bonificacao_concedida:,.2f}".replace('.', '#').replace(',', '.').replace('#', ','))
    print(f"Salário Final (Com Bônus): R$ {salario_final:,.2f}".replace('.', '#').replace(',', '.').replace('#', ','))